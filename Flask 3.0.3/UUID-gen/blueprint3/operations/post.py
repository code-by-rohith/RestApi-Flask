from flask import Blueprint, request, jsonify
from database.db import coll  

post_blueprint = Blueprint('post_blueprint', __name__)

@post_blueprint.route('/post', methods=['POST'])
def post():
    conn = request.get_json()
    new_war = {
        "country": conn["country"],
        "war": conn['war'],
    }
    coll.insert_one(new_war)
    return jsonify({"message": "inserted successfully"})
