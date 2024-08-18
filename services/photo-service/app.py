from flask import Flask, jsonify, request
from models import db, Photo
import redis
import pika
import json
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
db.init_app(app)

# Redis client
redis_client = redis.Redis.from_url(os.getenv('REDIS_URI'))

# RabbitMQ connection
connection = pika.BlockingConnection(pika.ConnectionParameters(os.getenv('RABBITMQ_URI')))
channel = connection.channel()
channel.queue_declare(queue='photo_uploads')

@app.route('/photos', methods=['GET'])
def get_photos():
    cached_photos = redis_client.get('all_photos')
    if cached_photos:
        return jsonify(json.loads(cached_photos))
    
    photos = Photo.query.all()
    photo_list = [{'id': p.id, 'url': p.url, 'caption': p.caption} for p in photos]
    
    redis_client.setex('all_photos', 3600, json.dumps(photo_list))  # Cache for 1 hour
    return jsonify(photo_list)

@app.route('/photos', methods=['POST'])
def upload_photo():
    data = request.json
    new_photo = Photo(user_id=data['user_id'], url=data['url'], caption=data['caption'])
    db.session.add(new_photo)
    db.session.commit()
    
    # Publish message to RabbitMQ
    channel.basic_publish(exchange='',
                          routing_key='photo_uploads',
                          body=json.dumps({'photo_id': new_photo.id, 'user_id': new_photo.user_id}))
    
    return jsonify({'message': 'Photo uploaded successfully', 'id': new_photo.id}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
