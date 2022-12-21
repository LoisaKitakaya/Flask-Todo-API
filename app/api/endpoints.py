from flask_restful import Resource, abort
from app.models.users import User
from app.models.todo import Todo
from .decorators import token_required
from .schema import user_schema, todo_schema, todos_schema

class UserEndpoint(Resource):

    @token_required
    def get(self, current_user):

        user = user_schema.dump(current_user)

        return {'data': user}, 200

class AllTodosEndpoint(Resource):

    @token_required
    def get(self, current_user):

        todos = Todo.query.filter_by(user_id=current_user.id)
        all_tasks = todos_schema.dump(todos)

        return {'data': {
            'owner': current_user.public_id,
            'payload': all_tasks
        }}, 200

class TodoEndpoint(Resource):

    @token_required
    def get(self, current_user, task_id):

        return {'message': 'working'}, 200
    
    @token_required
    def post(self, current_user):

        return {'message': 'working'}, 200
    
    @token_required
    def delete(self, current_user, task_id):

        return {'message': 'working'}, 200