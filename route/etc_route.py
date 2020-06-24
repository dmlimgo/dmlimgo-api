from flask import request
from flask_restplus import Namespace, Resource

api = Namespace('etc', path='/api/v1')

@api.route('/')
class Test(Resource):
    def get(self):
        """테스트용"""
        return 'Hello'