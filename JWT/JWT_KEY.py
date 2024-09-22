from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'welcome'
jwt = JWTManager(app)


users = {}
data = {}
current_id = 1

@app.route('/see', methods=['GET'])
def see():
    return jsonify({"Data": data})

@app.route('/register', methods=['POST'])
def register():
    global current_id
    username = request.json.get('username')
    password = request.json.get('password')

    if username in users:
        return jsonify({"msg": "User already exists"}), 400
    users[username] = password

    data[current_id] = {
        "username": username,
        "password": password
    }
    current_id += 1

    return jsonify({"msg": "User registered successfully", "user_id": current_id - 1}), 201
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    if users.get(username) != password:
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

if __name__ == '__main__':
    app.run(debug=True)
