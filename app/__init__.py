from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.urandom(24)
    app.config['SESSION_TYPE'] = 'filesystem'  # 서버 사이드 세션

    # instance 폴더 보장
    os.makedirs(app.instance_path, exist_ok=True)

    app.config['SQLALCHEMY_DATABASE_URI'] = (
        'sqlite:////home/kumo_cloud/local_restaurant_DB/instance/restaurants.db'
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    print("🔥 Flask DB PATH:", app.config['SQLALCHEMY_DATABASE_URI'])

    db.init_app(app)
    Session(app)  # 세션 초기화

    from app.routes import bp
    app.register_blueprint(bp)

    return app