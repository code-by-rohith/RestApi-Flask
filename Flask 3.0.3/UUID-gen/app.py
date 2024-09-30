from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

users = {}

@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    if 'name' not in data or 'roll' not in data:
        return jsonify({"error": "Please provide both name and roll number"}), 400

    user_id = str(uuid.uuid4())
    users[user_id] = {'name': data['name'], 'roll': data['roll']}
    return jsonify({"user_id": user_id, "message": "User created successfully"}), 201

@app.route('/user/<user_id>', methods=['GET'])
def get_user(user_id):
    if user_id in users:
        return jsonify({"user_id": user_id, "user": users[user_id]}), 200
    return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
