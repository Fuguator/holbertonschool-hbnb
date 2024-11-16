from flask import Flask
from flask_restx import Api
from app.api.v1.users import api as users_ns
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

def create_app(config_class="config.DevelopmentConfig"):
    #configuration
    app = Flask(__name__)
    app.config.from_object(config_class)
    api = Api(app, version='1.0', title='HBnB API', description='HBnB Application API')
    
    #bcrypt initialization
    bcrypt.init_app(app)

    api.add_namespace(users_ns, path='/api/v1/users')
    return app