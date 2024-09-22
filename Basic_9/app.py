from flask import Flask, render_template ,jsonify,request
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client['school']
students_collection = db['students']

def format_student(student):
    return {
        'id': str(student['_id']),
        'name': student['name'],
        'roll_no': student['roll_no']
    }

@app.route('/')
def index():
    students = list(students_collection.find())
    formatted_students = [format_student(student) for student in students]
    return render_template('login.html', students=formatted_students)

@app.route('/students', methods=['GET'])
def get_students():
    students = list(students_collection.find())
    return jsonify([format_student(student) for student in students]), 200

@app.route('/students', methods=['POST'])
def create_student():
    data = request.json
    new_student = {
        'name': data['name'],
        'roll_no': data['roll_no']
    }
    students_collection.insert_one(new_student)
    return jsonify({'message': 'Student added successfully'}),201

@app.route('/students/<string:id>', methods=['PUT'])
def update_student(id):
    data = request.json
    result = students_collection.update_one({'_id': ObjectId(id)}, {'$set': {
        'name': data['name'],
        'roll_no': data['roll_no']
    }})
    if result.matched_count == 0:
        return jsonify({'error': 'Student not found'}), 404
    return jsonify({'message': 'Student updated successfully'}), 200

@app.route('/students/<string:id>', methods=['DELETE'])
def delete_student(id):
    result = students_collection.delete_one({'_id': ObjectId(id)})
    if result.deleted_count == 0:
        return jsonify({'error': 'Student not found'}), 404
    return jsonify({'message': 'Student deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
