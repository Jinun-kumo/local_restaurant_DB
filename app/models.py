from app import db

class Restaurant(db.Model):
    __tablename__ = 'restaurants'   # ⭐ 이 줄 추가

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200))
    phone = db.Column(db.String(50))
    category = db.Column(db.String(50))

    reviews = db.relationship('Review', backref='restaurant', lazy=True)


class Review(db.Model):
    __tablename__ = 'reviews'        # ⭐ 이것도 같이 맞추자

    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(
        db.Integer,
        db.ForeignKey('restaurants.id'),  # ⭐ FK도 테이블명 맞춤
        nullable=False
    )
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text, nullable=False)

