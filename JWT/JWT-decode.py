from flask import Flask , request , jsonify
import jwt
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] =  '3hbj3bn4jh3b51n2nkj5nkjn65jk45n4jk10i21hu3jnjn'

@app.route('/login',methods =['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']

    token = jwt.encode({'sub':username ,
                        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=100)}
                        ,app.config['SECRET_KEY'],algorithm='HS256')
    
    return jsonify({"token":token})

@app.route('/read',methods =['POST'])
def read():
    data = request.get_json()
    token = data['token']
    tokens = jwt.decode(token , app.config['SECRET_KEY'],algorithms='HS256')
    return jsonify({"Token Data (username)":tokens['sub']})

if __name__ == '__main__':
    app.run(debug= True)