from flask import Flask
from flask_restful import Api

from config import configuration
from app.routes.notification import Notification
from app.extensions import database

def main(config_mode):
    
    application = Flask(__name__)
    application.config.from_object(configuration[config_mode])
    
    # initialize extensions
    database.init_app(application)
    
    api = Api(application)
    api.add_resource(Notification, "/notification")
    
    return application