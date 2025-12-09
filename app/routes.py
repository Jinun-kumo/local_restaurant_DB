from flask import Blueprint, render_template
from .models import Restaurant

bp = Blueprint('main', __name__)

@bp.route('/')
@bp.route('/restaurants')
def restaurant_list():
    restaurants = Restaurant.query.all()
    return render_template('restaurants.html', restaurants=restaurants)
