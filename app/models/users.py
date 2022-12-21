from app.extensions import db
from flask_login import UserMixin

class User(UserMixin, db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(256), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(254))
    todos = db.relationship('Todo', backref='user')
    tokens = db.relationship('UserToken', backref='user')

    def __repr__(self) -> str:
        
        return f'<User: "{self.email}">'

class UserToken(db.Model):

    __tablename__ = 'tokens'

    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(256))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self) -> str:
        
        return f'<UserToken: "{self.token}">'