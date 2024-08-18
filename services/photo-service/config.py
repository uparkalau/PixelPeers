from flask_migrate import Migrate
from models import db

def init_migrate(app):
    migrate = Migrate(app, db)
