from flask_restful import Resource, abort
from app.models.users import User, UserToken
from app.models.todo import Todo
from .decorators import token_required

class UserEndpoint(Resource):

    @token_required
    def get(self, current_user):

        return {'message': 'working'}, 200

class UserTokenEndpoint(Resource):

    @token_required
    def get(self, current_user):

        return {'message': 'working'}, 200

class TokenEndpoint(Resource):

    @token_required
    def get(self, current_user):

        return {'message': 'working'}, 200
    
    @token_required
    def post(self, current_user):

        return {'message': 'working'}, 200
    
    @token_required
    def delete(self, current_user):

        return {'message': 'working'}, 200