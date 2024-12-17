
from flask import Flask , jsonify 
from flask import Blueprint
from database import data_collection
from models import user_list_schema
from marshmallow import ValidationError

app = Flask(__name__)

get = Blueprint('get',__name__)


@get.route('/see', methods=['GET'])
def see():
    datas = list(data_collection.find({}, {"_id": 0}))
    try:
        validated_data = user_list_schema.dump(datas)
        return jsonify({"Data": validated_data}),200
    except ValidationError as err:
        return jsonify({"errors": err.messages}),400