from flask import Blueprint, request, jsonify
from app.models import create_user, get_user_by_id, update_user, delete_user

app_routes = Blueprint('app_routes', __name__)

@app_routes.route('/create_user', methods=['POST'])
def add_user():
    try:
        data = request.json
        if not all(key in data for key in ['username', 'email', 'password']):
            raise ValueError("Missing required fields: username, email, and password")
        
        create_user(data['username'], data['email'], data['password'])
        return jsonify({"message": "User created successfully!"}), 201
    except ValueError as e:
        return jsonify({"status": "error", "message": str(e)}), 400
    except Exception as e:
        return jsonify({"status": "error", "message": "Internal Server Error"}), 500

@app_routes.route('/get_user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = get_user_by_id(user_id)
    if user:
        return jsonify(dict(user))
    return jsonify({"message": "User not found!"}), 404

@app_routes.route('/update_user/<int:user_id>', methods=['PUT'])
def update_user_info(user_id):
    data = request.json
    update_user(user_id, data['username'], data['email'], data['password'])
    return jsonify({"message": "User updated successfully!"})

@app_routes.route('/delete_user/<int:user_id>', methods=['DELETE'])
def delete_user_info(user_id):
    delete_user(user_id)
    return jsonify({"message": "User deleted successfully!"})