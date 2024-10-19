from flask import Flask 
from flask import jsonify
from pymongo import MongoClient
import jwt
from flask import request
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] ='4h3jb5j3hb5jh35hj3b4hj5b2hj3bhj1b4jbkn5k463j6vkc34h6kb34kl6n3k4n6'

client = MongoClient('localhost',27017)
db = client['rohtih']
col = db['rohith_collection']



@app.route('/login',methods =['POST'])
def login():
    data = request.get_json()
    username =  data['username']
    keyword = data['keyword']
    token = jwt.encode({
        'sub':username,
        'exp' :datetime.datetime.utcnow() + datetime.timedelta(seconds=16)
    },app.config['SECRET_KEY'],algorithm='HS256')

  

    return jsonify({"message":"posted","token":token})


@app.route('/view',methods= ['POST'])
def view():
    data = request.get_json()
    values = data['token']
    if values:
        try:
            valuess = jwt.decode(values , app.config['SECRET_KEY'],algorithms='HS256')        
            filtered_sub = valuess['sub']
            return jsonify(filtered_sub)
        except jwt.ExpiredSignatureError:
            return jsonify({"message":"expired"})
        except jwt.InvalidSignatureError:
            return jsonify({"message":"invalid signature"})


if __name__ == '__main__':
    app.run(debug= True)