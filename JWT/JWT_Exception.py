from flask import Flask, request, jsonify
import datetime
import jwt
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)   

client = MongoClient('localhost', 27017)
db = client['protected']
col = db['secured']

app.config['SECRETKEY'] = 'ANKJSNKJNKJN'

@app.route("/")
def main():
    return "welcome"

@app.route('/login', methods=['POST'])
def login():
    data = request.json

    username = data.get('username')
    password = data.get('password')

    if not isinstance(data, dict) or 'username' not in data or 'password' not in data:
        return jsonify({"message": "error or incorrect password"}), 401

    existing_user = col.find_one({"username": username})
    workflow = jwt.encode({
        "sub": username,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=100)
    }, app.config['SECRETKEY'], algorithm='HS256')

    if existing_user:
        col.update_one({"username": username}, {"$set": {"token": workflow}})
        return jsonify({" message":f"Updated {username} sucessfully ","updated token":workflow})
    else:
        col.insert_one({"username": username, "token": workflow})

    return jsonify(workflow=workflow)

@app.route('/protected', methods=['POST'])
def check():
    data = request.json
    token = data.get('token')
    
    if token:
        try:
            find = jwt.decode(token, app.config['SECRETKEY'], algorithms=['HS256'])
            return jsonify({"username": find['sub']})
        
        except jwt.ExpiredSignatureError:
            return jsonify({"message": "token expired"}), 401
        
        except jwt.InvalidSignatureError:
            return jsonify({"message": "enter correct token"}), 401
        
    return jsonify({"message": "error or incorrect token"}), 401

@app.route('/get/<string:id>', methods=['GET'])
def getter(id):
    workflow = col.find_one({"_id": ObjectId(id)})

    if workflow:
        workflow['_id'] = str(workflow['_id'])  
        return jsonify(workflow), 200 
    
    return jsonify({"message": "Document not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)


"""
JWT, or JSON Web Token, is a method for securely transmitting information between two parties, like a client and a server. 
It helps verify a user's identity and allows access to resources without needing to log in repeatedly. 
When a user logs in, the server generates a JWT that contains user details and signs it to ensure its authenticity. 
The user then sends this token with their requests. This way, the server can trust the token and grant 
access based on the information inside it. 
JWTs are commonly used in web applications for authentication and data exchange.
"""
