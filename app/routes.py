from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import Restaurant, Review, User
from . import db

bp = Blueprint('main', __name__)

@bp.route('/')
@bp.route('/restaurants')
def restaurant_list():
    restaurants = Restaurant.query.all()
    return render_template('restaurants.html', restaurants=restaurants)

@bp.route('/restaurant/<int:restaurant_id>')
def restaurant_detail(restaurant_id):
    restaurant = Restaurant.query.get_or_404(restaurant_id)
    reviews = Review.query.filter_by(restaurant_id=restaurant_id).all()
    return render_template('restaurant_detail.html', restaurant=restaurant, reviews=reviews)

@bp.route('/restaurant/<int:restaurant_id>/review', methods=['POST'])
def add_review(restaurant_id):
    restaurant = Restaurant.query.get_or_404(restaurant_id)
    
    # Get form data
    username = request.form.get('username')
    rating = request.form.get('rating', type=int)
    comment = request.form.get('comment')
    
    # Get or create user
    user = User.query.filter_by(username=username).first()
    if not user:
        user = User(username=username, password='default')
        db.session.add(user)
        db.session.commit()
    
    # Create review
    review = Review(
        restaurant_id=restaurant_id,
        user_id=user.id,
        rating=rating,
        comment=comment
    )
    db.session.add(review)
    db.session.commit()
    
    flash('리뷰가 등록되었습니다!', 'success')
    return redirect(url_for('main.restaurant_detail', restaurant_id=restaurant_id))
