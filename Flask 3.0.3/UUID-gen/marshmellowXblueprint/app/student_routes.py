from flask import Blueprint, request, jsonify
from .schemas import student_schema, students_schema

student_bp = Blueprint('student_bp', __name__)

students = []

@student_bp.route('/', methods=['POST'])
def add_student():
    json_data = request.get_json()
    errors = student_schema.validate(json_data) 
    if errors:
        return jsonify(errors), 400
    student = student_schema.load(json_data)

    for existing_student in students:
        if existing_student.get('rollno') == student.get('rollno'):
            return jsonify({"message": "Student already exists"}), 400
    students.append(student)  

    return student_schema.dump(student), 201
@student_bp.route('/', methods=['GET'])
def get_students():
    return students_schema.dump(students), 200
