from flask import Flask, jsonify, request
from models import db, Profile
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

@app.route('/profiles', methods=['GET'])
def get_profiles():
    profiles = Profile.query.all()
    return jsonify([{'id': p.id, 'user_id': p.user_id, 'bio': p.bio, 'profile_picture_url': p.profile_picture_url} for p in profiles])

@app.route('/profiles/<int:user_id>', methods=['GET'])
def get_profile(user_id):
    profile = Profile.query.filter_by(user_id=user_id).first()
    if profile:
        return jsonify({'id': profile.id, 'user_id': profile.user_id, 'bio': profile.bio, 'profile_picture_url': profile.profile_picture_url})
    return jsonify({'error': 'Profile not found'}), 404

@app.route('/profiles', methods=['POST'])
def create_profile():
    data = request.json
    new_profile = Profile(user_id=data['user_id'], bio=data['bio'], profile_picture_url=data['profile_picture_url'])
    db.session.add(new_profile)
    db.session.commit()
    return jsonify({'message': 'Profile created successfully', 'id': new_profile.id}), 201

@app.route('/profiles/<int:user_id>', methods=['PUT'])
def update_profile(user_id):
    data = request.json
    profile = Profile.query.filter_by(user_id=user_id).first()
    if profile:
        profile.bio = data['bio']
        profile.profile_picture_url = data['profile_picture_url']
        db.session.commit()
        return jsonify({'message': 'Profile updated successfully'})
    return jsonify({'error': 'Profile not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
