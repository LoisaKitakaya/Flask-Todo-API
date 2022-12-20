from app.extensions import db

class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(256), unique=True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(100), unique=True)
    verified = db.Column(db.Boolean, default=False)
    password = db.Column(db.String(254))
    todos = db.relationship('todo.Todo', backref='user')

    def __repr__(self) -> str:
        
        return f'<User: "{self.username}">'