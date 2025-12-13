from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dev-key'

    os.makedirs(app.instance_path, exist_ok=True)
    db_path = os.path.join(app.instance_path, 'restaurants.db')

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/kumo_cloud/local_restaurant_DB/instance/restaurants.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    print("🔥 Flask DB PATH:", app.config['SQLALCHEMY_DATABASE_URI'])


    db.init_app(app)

    from app import routes
    app.register_blueprint(routes.bp)

    return app
