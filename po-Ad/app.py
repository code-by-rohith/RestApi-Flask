from flask import Flask, jsonify, request, make_response
from database import data_collection 
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from marshmallow import ValidationError 
from models import user_list_schema ,user_schema
from get import get


app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'welcome'
jwt = JWTManager(app)



app.register_blueprint(get)

@app.route('/register', methods=['POST'])
def register():
    temp = request.get_json()
    try:
        validated_data = user_schema.load(temp)
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400

    username = validated_data["name"]
    roll_no = validated_data["roll_no"]

    if data_collection.find_one({"roll_no": roll_no}):
        return jsonify({"msg": "User already exists"}), 400
       
    data_collection.insert_one({"name": username, "roll_no": roll_no})
    response = make_response(jsonify({"msg": "User registered successfully"}), 201)
    return response

@app.route('/login', methods=['POST'])
def login():
    temp = request.get_json()
    try:
        validated_data = user_schema.load(temp)
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400

    username = validated_data["name"]
    roll_no = validated_data["roll_no"]

    user = data_collection.find_one({"roll_no": roll_no})
    if user:
        access_token = create_access_token(identity=username)
        data_collection.update_one({"roll_no":roll_no},{"$set":{"access_token":access_token}})
        return jsonify({"message":"Sucessfully logged in","acess_token":access_token})
    return jsonify({"message": "No user found"}), 404


@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify({"message": f"Hello, {current_user}!"}), 200

if __name__ == '__main__':
    app.run(debug=True)
