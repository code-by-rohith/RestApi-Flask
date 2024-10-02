from flask import Blueprint, request, jsonify

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    name = data.get('name')
    username = data.get('username')
    if not name or not username:
        return jsonify({"error": "Both name and username are required"}), 400
    return jsonify({"name": name, "username": username}), 201
