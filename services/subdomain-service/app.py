from flask import Flask, jsonify, request
from models import db, Subdomain
import redis
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
db.init_app(app)

# Redis client
redis_client = redis.Redis.from_url(os.getenv('REDIS_URI'))

@app.route('/subdomains', methods=['GET'])
def get_subdomains():
    subdomains = Subdomain.query.all()
    return jsonify([{'id': s.id, 'name': s.name, 'user_id': s.user_id} for s in subdomains])

@app.route('/subdomains', methods=['POST'])
def create_subdomain():
    data = request.json
    new_subdomain = Subdomain(name=data['name'], user_id=data['user_id'])
    db.session.add(new_subdomain)
    db.session.commit()
    return jsonify({'message': 'Subdomain created successfully', 'id': new_subdomain.id}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)
