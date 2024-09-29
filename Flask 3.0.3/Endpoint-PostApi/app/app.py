from flask import Flask,request ,jsonify
app= Flask(__name__)

datas=[]

@app.route('/post/<int:id>',methods=['POST','GET'])
def main(id):
    if request.method =='POST':
        data=request.json
        global datas
        datas.append(data)
        print(datas)
        return jsonify({f"INSERTED id - {id}:":data}),201
    return jsonify({"Server Error"}),404



if __name__ == '__main__':
    app.run(debug=True)