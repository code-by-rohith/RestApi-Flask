from flask import Flask, request, jsonify
import jwt
import datetime

app = Flask(__name__)

SECRET_KEY = 'DADADA' 
users = {'test': 'test123'}  

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if users.get(username) == password:
     
        token = jwt.encode({
            'sub': username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=1)  # Token expires in 1 minute
        }, SECRET_KEY, algorithm='HS256')
        return jsonify(token=token), 200
    
    return jsonify(message='Invalid credentials!'), 401

@app.route('/protected', methods=['GET'])
def protected():
    token = request.headers.get('Authorization')
    
    if not token:
        return jsonify(message='Token is missing!'), 403
    
    try:
 
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return jsonify(message=f'Hello, {payload["sub"]}!'), 200
    except jwt.ExpiredSignatureError:
        return jsonify(message='Token has expired!'), 401
    except jwt.InvalidTokenError:
        return jsonify(message='Invalid token!'), 401

if __name__ == '__main__':
    app.run(port=8888, debug=True)
