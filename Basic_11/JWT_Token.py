from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from pymongo import MongoClient

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'Rohith0224535443343543548Rohith'
jwt = JWTManager(app)

client = MongoClient("mongodb://localhost:27017/")
db = client['workflow_']
collections_flow = db['market']

def helperfunction(market):
    return {
        'id': str(market['_id']),
        'name': market['name'],
        'price': market['price']
    }

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    if username == 'admin' and password == 'password':  # Simple example
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/students', methods=['GET'])
@jwt_required()
def getting():
    conn = list(collections_flow.find())
    return jsonify([helperfunction(market) for market in conn]), 200

@app.route('/students', methods=['POST'])
@jwt_required()
def posting():
    reports = request.json
    if isinstance(reports, list):
        result = collections_flow.insert_many(reports)
        return jsonify({'message': "Successfully posted", 'ids': [str(id) for id in result.inserted_ids]}), 201
    elif isinstance(reports, dict):
        result = collections_flow.insert_one(reports)
        return jsonify({'message': "Successfully posted", 'id': str(result.inserted_id)}), 201
    return jsonify({'message': "Invalid input format. Must be a list or a single document."}), 400



if __name__ == '__main__':
    app.run(debug=True, port=5000)
