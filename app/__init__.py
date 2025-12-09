from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    # Instance 폴더 생성
    os.makedirs(app.instance_path, exist_ok=True)

    # DB 파일 경로 설정
    db_path = os.path.join(app.instance_path, 'restaurants.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # 라우트 추가
    from . import routes
    app.register_blueprint(routes.bp)

    return app
