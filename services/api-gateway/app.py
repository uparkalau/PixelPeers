from flask import Flask, jsonify, request
import requests
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Load environment variables
USER_SERVICE_URL = os.getenv('USER_SERVICE_URL')
PHOTO_SERVICE_URL = os.getenv('PHOTO_SERVICE_URL')
PROFILE_SERVICE_URL = os.getenv('PROFILE_SERVICE_URL')
TEMPLATE_SERVICE_URL = os.getenv('TEMPLATE_SERVICE_URL')
SUBDOMAIN_SERVICE_URL = os.getenv('SUBDOMAIN_SERVICE_URL')

SERVICES = {
    'user': USER_SERVICE_URL,
    'photo': PHOTO_SERVICE_URL,
    'profile': PROFILE_SERVICE_URL,
    'template': TEMPLATE_SERVICE_URL,
    'subdomain': SUBDOMAIN_SERVICE_URL
}

@app.route('/<service>/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def proxy(service, path):
    if service in SERVICES:
        try:
            response = requests.request(
                method=request.method,
                url=f"{SERVICES[service]}/{path}",
                headers={key: value for (key, value) in request.headers if key != 'Host'},
                data=request.get_data(),
                cookies=request.cookies,
                allow_redirects=False
            )
            headers = {key: value for (key, value) in response.headers.items()}
            return (response.content, response.status_code, headers)
        except requests.RequestException as e:
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify({"error": "Service not found"}), 404

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    host_header = request.headers.get('Host', '')
    if '.' in host_header:
        subdomain = host_header.split('.')[0]
        try:
            response = requests.get(f"{SERVICES['subdomain']}/resolve/{subdomain}")
            if response.status_code == 200:
                user_id = response.json().get('user_id')
                if user_id:
                    photos_response = requests.get(f"{SERVICES['photo']}/photos/user/{user_id}")
                    template_response = requests.get(f"{SERVICES['template']}/templates/user/{user_id}")

                    if photos_response.status_code == 200 and template_response.status_code == 200:
                        photos = photos_response.json()
                        template = template_response.json()
                        return jsonify({'photos': photos, 'template': template})
                    else:
                        return jsonify({"error": "Failed to fetch photos or template"}), 500
            return jsonify({"error": "Subdomain not found"}), 404
        except requests.RequestException as e:
            return jsonify({"error": str(e)}), 500
    return jsonify({"error": "Invalid Host header"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
