from app import app
from app.models import Movies

@app.route('/get-all')
def getAll():
    allMovies = Movies.query.all()#
    titles = ""
    for i in allMovies:
        titles += i.title
    return titles