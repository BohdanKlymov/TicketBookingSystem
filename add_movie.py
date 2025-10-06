from app import app, db
from app.models import Movies

with app.app_context():
    db.create_all()

    new_movie = Movies(title="Alice", price=34.25, seats=50, available_seats=34)
    db.session.add(new_movie)
    db.session.commit()
    print("✅ Movie added successfully!")
