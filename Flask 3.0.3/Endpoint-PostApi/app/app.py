from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson.json_util import dumps

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://mongo:27017/studentdb"
mongo = PyMongo(app)

@app.route('/students', methods=['POST'])
def add_student():
    name = request.json.get('name')
    roll = request.json.get('roll')
    
    if not name or not roll:
        return jsonify({"error": "Name and roll are required"}), 400
    
    mongo.db.students.insert_one({'name': name, 'roll': roll})
    return jsonify({"message": "Student added successfully"}), 201

@app.route('/students', methods=['GET'])
def get_students():
    students = mongo.db.students.find()
    return dumps(students), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
