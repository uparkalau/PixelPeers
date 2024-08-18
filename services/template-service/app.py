from flask import Flask, jsonify, request
from models import db, Template
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

@app.route('/templates', methods=['GET'])
def get_templates():
    templates = Template.query.all()
    return jsonify([{'id': t.id, 'user_id': t.user_id, 'content': t.content} for t in templates])

@app.route('/templates/<int:template_id>', methods=['PUT'])
def update_template(template_id):
    template = Template.query.get_or_404(template_id)
    data = request.json
    template.content = data['content']
    db.session.commit()
    return jsonify({'message': 'Template updated successfully'})

@app.route('/templates/user/<int:user_id>', methods=['GET'])
def get_user_template(user_id):
    template = Template.query.filter_by(user_id=user_id).first()
    if template:
        return jsonify({'id': template.id, 'content': template.content})
    return jsonify({'error': 'Template not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)
