from flask import Flask, request, jsonify, make_response, render_template, session, flash
import jwt
from datetime import datetime, timedelta, timezone
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired!'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token!'}), 403

        return f(*args, **kwargs)

    return decorated


@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return 'Logged in currently'


@app.route('/public')
def public():
    return 'This is a public endpoint.'


@app.route('/auth')
@token_required
def auth():
    return 'JWT is verified. Welcome to your dashboard!'


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username == 'user' and password == '123456':
        session['logged_in'] = True

        token = jwt.encode({
            'user': username,
            'exp': datetime.now(timezone.utc) + timedelta(seconds=60)
        }, app.config['SECRET_KEY'], algorithm="HS256")

        return jsonify({'token': token})
    else:
        flash('Invalid credentials. Please try again.')
        return make_response('Unable to verify', 403)


@app.route('/logout', methods=['POST'])
def logout():
    session.pop('logged_in', None)
    return jsonify({'message': 'Successfully logged out!'})


if __name__ == "__main__":
    app.run(debug=True)
