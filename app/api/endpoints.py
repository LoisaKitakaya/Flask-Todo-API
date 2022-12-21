from flask_restful import Resource, abort
from flask import request
from app.models.users import User
from app.models.todo import Todo
from app.extensions import db
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

    @token_required
    def post(self, current_user):

        task = request.get_json()
        task['user_id'] = current_user.id if current_user else None


        new_task = todo_schema.load(task)

        try:

            db.session.add(new_task)

        except:

            abort(500, message='Something went wrong.')

        else:

            db.session.commit()

        return {'data': {
            'owner': current_user.public_id if current_user else None,
            'payload': todo_schema.dump(new_task)
        }}, 200

class TodoEndpoint(Resource):

    @token_required
    def get(self, current_user, task_id):

        try:

            task = Todo.query.filter_by(
                id=int(task_id), user_id=current_user.id
            ).first()

        except:

            abort(404, message='Task not found.')

        else:

            this_task = todo_schema.dump(task)

        return {'data': {
            'owner': current_user.public_id,
            'payload': this_task
        }}, 200
    
    @token_required
    def delete(self, current_user, task_id):

        try:

            task = Todo.query.filter_by(
                id=int(task_id), user_id=current_user.id
            ).first()

        except:

            abort(404, message='Task not found.')

        else:

            try:

                db.session.delete(task)

            except:

                abort(404, message='Task not found.')
            
            else:

                db.session.commit()

        return {'data': {
            'owner': current_user.public_id,
            'message': 'Deleted successfully.'
        }}, 200