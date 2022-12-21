from app.extensions import db, ma
from app.models.users import User
from app.models.todo import Todo

class UserSchema(ma.SQLAlchemyAutoSchema):

    class Meta:

        model = User
        load_instance = True
        sqla_session = db.session

class TodoSchema(ma.SQLAlchemyAutoSchema):

    class Meta:

        model = Todo
        include_fk = True
        load_instance = True
        sqla_session = db.session

user_schema = UserSchema()
todo_schema = TodoSchema()
todos_schema = TodoSchema(many=True)