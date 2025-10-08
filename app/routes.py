from app import app
from app.models import Movies
from flask import jsonify

@app.route('/get-all')
def getAll():
    allMovies = Movies.query.all()
    moviesList = []
    for i in allMovies:
        moviesList.append(i.to_dict())
    return jsonify(moviesList)