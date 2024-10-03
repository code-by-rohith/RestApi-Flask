from flask import Blueprint, request, jsonify
from .base import detailed_data, obj_tendancy_alort_single, obj_tendancy_alort_multiple
from db.datas import data, train_data

appbase = Blueprint('appbase', __name__)

@appbase.route('/', methods=['GET'])
def main():
    errors = detailed_data.validate(data)
    if errors:
        return jsonify(errors), 400
    return jsonify(detailed_data.dump(data)), 200

@appbase.route('/train', methods=['GET'])
def train():
    req = train_data
    error = obj_tendancy_alort_multiple.validate(req)
    if error:
        return jsonify(error), 400
    return jsonify(obj_tendancy_alort_multiple.dump(req)), 200

@appbase.route('/train', methods=['POST'])
def train_post():
    conn = request.get_json()
    errors = obj_tendancy_alort_single.validate(conn)
    if errors:
        return jsonify(errors), 400
    subset = obj_tendancy_alort_single.load(conn)
    train_data.append(subset)
    return jsonify(obj_tendancy_alort_single.dump(subset)), 201
