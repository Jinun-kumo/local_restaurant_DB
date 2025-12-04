from app import db

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200))
    phone = db.Column(db.String(50))
    category = db.Column(db.String(50))

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text)
