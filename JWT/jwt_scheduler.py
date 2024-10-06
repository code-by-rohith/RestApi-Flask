from flask import Flask, request, jsonify
import datetime
import jwt
from pymongo import MongoClient
from bson import ObjectId
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client['protected']
col = db['secured']

app.config['SECRETKEY'] = 'ANKJSNKJNKJN'

users = {"rohith": "123456"}

def delete_expired_tokens():
    expired_tokens = col.find() 

    deleted_tokens = [] 

    for token in expired_tokens:
        try:
            jwt.decode(token['token'], app.config['SECRETKEY'], algorithms=['HS256'])

        except jwt.ExpiredSignatureError:
            col.delete_one({"_id": token["_id"]})
            deleted_tokens.append(token['token'])  

    if deleted_tokens:
        print(f"Deleted tokens: {deleted_tokens}")  

@app.route("/")
def main():
    return "Welcome"

@app.route('/login', methods=['POST'])
def login():
    data = request.json

    username = data.get('username')
    password = data.get('password')

    if not isinstance(data, dict) or 'username' not in data or 'password' not in data:
        return jsonify({"message": "Error: Missing username or password"}), 400
    
    existing_user = col.find_one({"username": username})

    if existing_user:
        workflow = jwt.encode({
            "sub": username,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=20) 
        }, app.config['SECRETKEY'], algorithm='HS256')

        col.update_one({"username": username}, {"$set": {"token": workflow}})

        return jsonify({"message": "Token updated", "workflow": workflow}), 200
    
    if username in users and users[username] == password:
        workflow = jwt.encode({
            "sub": username,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=20)  
        }, app.config['SECRETKEY'], algorithm='HS256')

        col.insert_one({"username": username, "token": workflow})

        return jsonify(workflow=workflow), 200

    return jsonify({"message": "Invalid username or password"}), 401

@app.route('/protected', methods=['POST'])
def check():
    data = request.json
    token = data.get('token')
    
    if token:
        try:
            find = jwt.decode(token, app.config['SECRETKEY'], algorithms=['HS256'])
            return jsonify({"username": find['sub']}), 200
        except jwt.ExpiredSignatureError:
            return jsonify({"message": "Token expired"}), 401
        except jwt.InvalidSignatureError:
            return jsonify({"message": "Invalid token"}), 401
    
    return jsonify({"message": "Token is missing"}), 400

@app.route('/get/<string:id>', methods=['GET'])
def getter(id):
    workflow = col.find_one({"_id": ObjectId(id)})

    if workflow:
        workflow['_id'] = str(workflow['_id'])  
        return jsonify(workflow), 200 
    return jsonify({"message": "Document not found"}), 404

if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(delete_expired_tokens, 'interval', seconds=20)  
    scheduler.start()
    
    try:
        app.run(debug=True)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
