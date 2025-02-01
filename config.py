import os

class Config:
    DATABASE = os.path.join(os.path.dirname(__file__), 'users.db')  # SQLite 数据库文件存储在项目根目录
    SECRET_KEY = 'your-secret-key'  # 用于 session 和其他加密
