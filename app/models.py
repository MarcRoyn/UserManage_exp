import sqlite3
import os
from flask import current_app, g

# 获取数据库连接
def get_db():
    db_path = current_app.config['DATABASE']
    print(f"Attempting to connect to database at: {db_path}")  # 打印数据库路径，用于调试
    
    # 确保数据库文件所在的目录存在
    db_folder = os.path.dirname(db_path)
    if not os.path.exists(db_folder):
        os.makedirs(db_folder)  # 如果目录不存在，创建它
        print(f"Directory created: {db_folder}")
    
    if 'db' not in g:
        g.db = sqlite3.connect(db_path)  # 连接数据库
        g.db.row_factory = sqlite3.Row  # 使得查询结果可以按字段名访问
    return g.db

# 关闭数据库连接
def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

# 创建用户表
def init_db():
    db = get_db()
    with current_app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

# 用户模型：原生 SQL 实现增删改查
def create_user(username, email, password):
    db = get_db()
    db.execute(
        "INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
        (username, email, password)
    )
    db.commit()

def get_user_by_id(user_id):
    db = get_db()
    user = db.execute(
        "SELECT * FROM users WHERE id = ?", (user_id,)
    ).fetchone()
    return user

def get_user_by_username(username):
    db = get_db()
    user = db.execute(
        "SELECT * FROM users WHERE username = ?", (username,)
    ).fetchone()
    return user

def update_user(user_id, username, email, password):
    db = get_db()
    db.execute(
        "UPDATE users SET username = ?, email = ?, password = ? WHERE id = ?",
        (username, email, password, user_id)
    )
    db.commit()

def delete_user(user_id):
    db = get_db()
    db.execute("DELETE FROM users WHERE id = ?", (user_id,))
    db.commit()
