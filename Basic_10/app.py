from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client['workflow_']
collections_flow = db['market']

def helperfunction(market):
    return {
        'id': str(market['_id']),
        'name': market['name'],
        'price': market['price']
    }
@app.route('/students', methods=['GET'])
def getting():
    conn = list(collections_flow.find())
    return jsonify([helperfunction(market) for market in conn]), 200

@app.route('/students', methods=['POST'])
def posting():
    reports = request.json
    if isinstance(reports, list):
        result = collections_flow.insert_many(reports)
        return jsonify({'message': "Successfully posted", 'ids': [str(id) for id in result.inserted_ids]}), 201
    elif isinstance(reports, dict):
        result = collections_flow.insert_one(reports)
        return jsonify({'message': "Successfully posted", 'id': str(result.inserted_id)}), 201
    return jsonify({'message': "Invalid input format. Must be a list or a single document."}), 400

@app.route('/students/<string:id>', methods=['PUT'])
def putting(id):
    report = request.json
    result = collections_flow.update_one(
        {'_id': ObjectId(id)},
        {'$set': {
            'name': report.get('name'),
            'price': report.get('price')
        }}
    )
    if result.matched_count == 0:
        return jsonify({"message": "Document not found"}), 404
    return jsonify({"message": "Updated successfully"}), 200

@app.route('/students/<string:id>', methods=['DELETE'])
def deleting(id):
    result = collections_flow.delete_one({'_id': ObjectId(id)})
    if result.deleted_count == 0:
        return jsonify({"message": "Document not found"}), 404
    return jsonify({"message": "Deleted successfully"}), 200

@app.route('/students/delete-many', methods=['DELETE'])
def delete_many():
    ids = request.json.get('ids', [])
    if not isinstance(ids, list):
        return jsonify({'message': 'Invalid input format. Must be a list of IDs.'}), 400

    object_ids = []
    for id in ids:
        try:
            object_ids.append(ObjectId(id))
        except Exception:
            return jsonify({'message': f'Invalid ID format: {id}'}), 400

    result = collections_flow.delete_many({'_id': {'$in': object_ids}})
    return jsonify({'message': f'{result.deleted_count} documents deleted successfully'}), 200

@app.route('/students/update-many', methods=['PUT'])
def update_many():
    updates = request.json
    if not isinstance(updates, list):
        return jsonify({'message': 'Invalid input format. Must be a list of update objects.'}), 400
    bulk_operations = []
    for update in updates:
        if not isinstance(update, dict) or 'id' not in update or 'fields' not in update:
            return jsonify({'message': 'Each update object must contain "id" and "fields".'}), 400
        try:
            object_id = ObjectId(update['id'])
            fields = update['fields']
            bulk_operations.append({
                'update_one': {
                    'filter': {'_id': object_id},
                    'update': {'$set': fields}
                }
            })
        except Exception:
            return jsonify({'message': f'Invalid ID format: {update["id"]}'}), 400

    result = collections_flow.bulk_write(bulk_operations)
    return jsonify({'message': f'{result.modified_count} documents updated successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
