from flask import Flask
from flask_restx import Api
from flask_jwt_extended import JWTManager
from app.api.v1.users import api as users_ns
from app.api.v1.auth import api as auth_ns
from app.api.v1.places import api as places_ns
from flask_bcrypt import Bcrypt
from config import config

bcrypt = Bcrypt()
jwt = JWTManager()

def create_app(config_name='development'):
    """App configuration"""
    app = Flask(__name__)
    
    app.config.from_object(config[config_name])
    
    if isinstance(config_name, str) and config_name.startswith('config.'):
        app.config.from_object(config_name)

    bcrypt.init_app(app)
    jwt.init_app(app)

    api = Api(app, version='1.0', title='HBnB API',
              description='HBnB Application API')

    api.add_namespace(users_ns, path='/api/v1/users')
    api.add_namespace(auth_ns, path='/api/v1/auth')
    api.add_namespace(places_ns, path='/api/v1/places')

    return app