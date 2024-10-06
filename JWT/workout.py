from flask import Flask,request , jsonify
import datetime
import jwt

app= Flask(__name__)

SECRETKEY ='ANKJSNKJNKJN'


users={"rohith":"123456"}

@app.route("/")
def main():
    return "welcome"

@app.route('/login',methods=['POST'])
def login():
    data = request.json

    username = data.get('username')
    password = data.get('password')

    if users.get(username) != password:
        return jsonify({"message":"error or inccorect password"}),404
    
    wrokflow= jwt.encode({
        "sub":username ,
        "exp" : datetime.datetime.utcnow() + datetime.timedelta(minutes=1)

    } , SECRETKEY ,algorithm='HS256')

    return jsonify(wrokflow=wrokflow)


    
    



if __name__ == '__main__':
    app.run(debug=True)