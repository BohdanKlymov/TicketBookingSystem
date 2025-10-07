from app import app, db
from app.models import Movies

with app.app_context():
    db.create_all()

    new_movie = Movies(title="Alice", price=34.25, \
                       movie_description="Alice left her home to find her dad", movie_picture = 'dowload (2).jpg)')
    db.session.add(new_movie)
    db.session.commit()
    print("✅ Movie added successfully!")
