from app import db
from app import app

class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    price = db.Column(db.Float())
    seats = db.Column(db.Integer())
    available_seats = db.Column(db.Integer())

    def __repr__(self):
        return f"<Movie {self.title}>"