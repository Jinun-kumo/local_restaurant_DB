from flask import Flask

def create_app():
    app = Flask(__name__)
    # 설정 예: app.config['SECRET_KEY'] = 'your-secret-key'

    @app.route('/')
    def home():
        return "Hello, Local 맛집 프로젝트!"

    return app