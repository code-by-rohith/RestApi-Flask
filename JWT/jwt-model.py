from flask import Flask, render_template, session, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, decode_token, get_jwt_identity

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = "DADADA"
app.config['SECRET_KEY'] = "s3wsw"
jwt = JWTManager(app)

@app.route('/')
def main():
    return render_template('index.html', access_token=None)

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    access_token = create_access_token(identity=username)
    session['jwt'] = access_token
    return render_template('index.html', access_token=access_token)

@app.route('/protected', methods=['POST'])
def protected():
    token = request.form.get('token') 
    if token: 
        try:
            decoded_token = decode_token(token)
            username = decoded_token['sub']
            time=decoded_token['iat']
            return jsonify(message=f'Hello, {username}! and {time}'),201
        except Exception:
            return jsonify(message='Invalid token!'), 401
    return jsonify(message='No token provided!'), 400

if __name__ == '__main__':
    app.run(debug=True)

