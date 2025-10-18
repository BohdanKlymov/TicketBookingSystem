from app import db
from app import app

class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    price = db.Column(db.Float())
    movie_description = db.Column(db.String(255))
    movie_yearOfRelease = db.Column(db.String(128))
    movie_picture = db.Column(db.String(255))

    # def __repr__(self):
    #     return f"Movie: <br>title - {self.title}\
    #           <br>price - {self.price} <br>description - {self.movie_description} {self.movie_picture}"  
    
    def to_dict(self):
        return {"title": self.title, "price": self.price, "movie_description": self.movie_description, "movie_yearOfRelease": self.movie_yearOfRelease, "movie_picture": self.movie_picture}