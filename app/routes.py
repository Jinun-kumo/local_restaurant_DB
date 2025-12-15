from flask import (
    Blueprint, render_template, request,
    redirect, url_for, session, flash
)
from sqlalchemy import func
from sqlalchemy.exc import IntegrityError
from app import db
from app.models import Restaurant, Review, User

bp = Blueprint('main', __name__)

# --------------------
# 메인 페이지
# --------------------
@bp.route('/')
def index():
    restaurants = Restaurant.query.all()
    for r in restaurants:
        avg = db.session.query(func.avg(Review.rating)).filter(Review.restaurant_id == r.id).scalar()
        r.average_rating = round(avg, 1) if avg else None
    return render_template('restaurants.html', restaurants=restaurants)


# --------------------
# 맛집 상세
# --------------------
@bp.route('/restaurant/<int:restaurant_id>')
def restaurant_detail(restaurant_id):
    restaurant = Restaurant.query.get_or_404(restaurant_id)

    avg_rating = db.session.query(
        func.avg(Review.rating)
    ).filter(
        Review.restaurant_id == restaurant_id
    ).scalar()

    print(f"Session user_id: {session.get('user_id')}")

    return render_template(
        'restaurant_detail.html',
        restaurant=restaurant,
        avg_rating=round(avg_rating, 1) if avg_rating else None
    )


# --------------------
# 리뷰 작성
# --------------------
@bp.route('/restaurant/<int:restaurant_id>/review', methods=['POST'])
def add_review(restaurant_id):
    if 'user_id' not in session:
        flash('로그인이 필요합니다.')
        return redirect(url_for('main.login'))

    review = Review(
        restaurant_id=restaurant_id,
        user_id=session['user_id'],
        rating=request.form['rating'],
        comment=request.form['comment']
    )

    db.session.add(review)
    db.session.commit()

    return redirect(url_for(
        'main.restaurant_detail',
        restaurant_id=restaurant_id
    ))


# --------------------
# 회원가입
# --------------------
@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user = User(username=request.form['username'])
        user.set_password(request.form['password'])

        try:
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('main.login'))
        except IntegrityError:
            db.session.rollback()
            flash('이미 존재하는 아이디입니다.')

    return render_template('register.html')


# --------------------
# 로그인
# --------------------
@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(
            username=request.form['username']
        ).first()

        if user and user.check_password(request.form['password']):
            session['user_id'] = user.id
            print(f"User {user.username} logged in with id {user.id}")
            return redirect(url_for('main.index'))

        flash('로그인 실패')

    return render_template('login.html')


# --------------------
# 로그아웃
# --------------------
@bp.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('main.index'))
