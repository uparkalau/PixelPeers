import os

class Config:
    USER_SERVICE_URL = os.getenv('USER_SERVICE_URL', 'http://user-service:5001')
    PHOTO_SERVICE_URL = os.getenv('PHOTO_SERVICE_URL', 'http://photo-service:5002')
    PROFILE_SERVICE_URL = os.getenv('PROFILE_SERVICE_URL', 'http://profile-service:5003')
    TEMPLATE_SERVICE_URL = os.getenv('TEMPLATE_SERVICE_URL', 'http://template-service:5004')
    SUBDOMAIN_SERVICE_URL = os.getenv('SUBDOMAIN_SERVICE_URL', 'http://subdomain-service:5005')
