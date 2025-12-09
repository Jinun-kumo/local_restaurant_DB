from app import create_app, db
import app.models  # 모델 인식시키기

app = create_app()

# 앱 시작 전 DB 생성
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
