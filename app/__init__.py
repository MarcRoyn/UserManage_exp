from flask import Flask,jsonify
from .routes import app_routes  # 导入路由

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    # 注册错误处理器
    register_error_handlers(app)

    # 注册路由
    app.register_blueprint(app_routes)  # 注册 Blueprint 路由

    return app

# 错误处理函数
def register_error_handlers(app):
    @app.errorhandler(404)
    def handle_404_error(error):
        response = {"status": "error", "message": "Resource not found"}
        return jsonify(response), 404

    @app.errorhandler(400)
    def handle_400_error(error):
        response = {"status": "error", "message": "Bad Request"}
        return jsonify(response), 400

    @app.errorhandler(500)
    def handle_500_error(error):
        response = {"status": "error", "message": "Internal Server Error"}
        return jsonify(response), 500

    @app.errorhandler(Exception)
    def handle_generic_error(error):
        response = {"status": "error", "message": str(error)}
        return jsonify(response), 500
