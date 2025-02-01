from app import create_app
from app.models import init_db

app = create_app()

# 在启动时初始化数据库
with app.app_context():
    init_db()

if __name__ == '__main__':
    app.run(debug=True)
