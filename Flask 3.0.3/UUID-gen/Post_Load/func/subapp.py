from flask import Flask, jsonify, Blueprint, request
from base.structure import obj, obj_many

appsite = Blueprint("appsite", __name__)

Data = []

@appsite.route('/get', methods=['GET'])
def getter():
    output_data = []
    for student in Data:
        student_with_total = student.copy()   
        output_data.append(student_with_total)
    
    return jsonify(obj_many.dump(output_data)), 200  

@appsite.route('/post', methods=['POST'])
def poster():
    req = request.get_json()
    if not req:
        return jsonify({"message": "No data provided"}), 400  

    errors = obj.validate(req)
    if errors:
        return jsonify({"message": errors}), 400  

    try:
        reqq = obj.load(req) 
        Data.append(reqq)      
    except Exception as e:
        return jsonify({"message": str(e)}), 500  
    print(Data)

    return jsonify({"message": "Successfully posted", "data": reqq}), 201  


