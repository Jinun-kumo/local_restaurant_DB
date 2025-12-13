from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Restaurant, Review

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    restaurants = Restaurant.query.all()
    return render_template('restaurants.html', restaurants=restaurants)


@bp.route('/restaurant/<int:restaurant_id>')
def restaurant_detail(restaurant_id):
    restaurant = Restaurant.query.get_or_404(restaurant_id)
    return render_template(
        'restaurant_detail.html',
        restaurant=restaurant
    )


@bp.route('/restaurant/<int:restaurant_id>/review', methods=['POST'])
def add_review(restaurant_id):
    rating = request.form['rating']
    comment = request.form['comment']

    review = Review(
        restaurant_id=restaurant_id,
        rating=rating,
        comment=comment
    )

    db.session.add(review)
    db.session.commit()

    # ⭐ 핵심: POST 후 무조건 redirect
    return redirect(url_for('main.restaurant_detail', restaurant_id=restaurant_id))
