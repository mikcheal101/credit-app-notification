from flask_restful import Resource
from flask import jsonify

class Notification(Resource):
    
    def get(self):
        return jsonify(status=200, message="hello world")