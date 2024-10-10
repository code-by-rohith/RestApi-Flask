from flask import Flask , request , jsonify

app = Flask(__name__)

data= []
@app.route("/login",methods =['POST'])
def main():
    value = request.get_json()
    username = value["username"]
    data.append({"seeded username":username})
    return jsonify({"message":"seeded in data "})

@app.route("/login",methods = ['GET'])
def main2():
    return jsonify(data)
        


if __name__ == '__main__':
    app.run(debug= True)