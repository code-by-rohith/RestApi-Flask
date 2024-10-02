from flask import Blueprint, jsonify
from database.db import coll  

get_blueprint = Blueprint('get_blueprint', __name__)

def helper(student):
    return {
        "id": str(student['_id']),
        "country": student["country"],
        "war": student['war']
    }

@get_blueprint.route('/get', methods=['GET'])
def get():
    conn = list(coll.find())
    return jsonify([helper(student) for student in conn])
