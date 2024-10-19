from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

    def to_dict(self):
        return {"username": self.username}

# Create the database
with app.app_context():
    db.create_all()

# Route to create a user
@app.route('/api/v1/users/<string:username>', methods=['POST'])
def create_user(username):
    if User.query.filter_by(username=username).first():
        return jsonify({"message": "User already exists"}), 400

    password = request.json.get('password')
    if not password:
        return jsonify({"message": "Password is required"}), 400

    hashed_password = generate_password_hash(password)
    new_user = User(username=username, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created", "username": username}), 201

# Route to get a specific user
@app.route('/api/v1/users/<string:username>', methods=['GET'])
def get_user(username):
    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify(user.to_dict())
    return jsonify({"message": "User not found"}), 404

# Route to delete a user
@app.route('/api/v1/users/<string:username>', methods=['DELETE'])
def delete_user(username):
    user = User.query.filter_by(username=username).first()
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "User deleted"}), 200
    return jsonify({"message": "User not found"}), 404

# Route to get all users
@app.route('/api/v1/users', methods=['GET'])
def get_all_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

if __name__ == '__main__':
    app.run(debug=True)