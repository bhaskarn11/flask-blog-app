from src import db


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(length=30), nullable=False)
    email = db.Column(db.String(length=64), nullable=False)
    sent_date = db.Column(db.DateTime, nullable=False)
    message = db.Column(db.Text(length=150), nullable=False)
    

    def __repr__(self):
        return f"ID:{self.id}, name: {self.name}, {self.email}, message: {self.message}, sent_date: {self.sent_date}"
