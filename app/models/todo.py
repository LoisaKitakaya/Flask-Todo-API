from app.extensions import db

class Todo(db.Model):

    __tablename__ = 'todo'
    
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(100))
    label = db.Column(db.String(50))
    description = db.Column(db.Text)
    due_date = db.Column(db.String(50))
    status = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self) -> str:
        
        return f'<Todo: "{self.task}">'