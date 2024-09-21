from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)
client = MongoClient('localhost', 27017)
db = client.login
student = db.student

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method=='GET':
        student_col = student.find()
        return render_template('index.html', student=student_col)
    elif request.method == 'POST':
        content = request.form['content']
        degree = request.form['degree']
        extra_content=request.form['extra_content']
        student.insert_one({'content': content, 'degree': degree,'Notes':extra_content})
        return redirect(url_for('index'))
    
@app.route('/<id>/delete/',methods=['POST'])
def delete(id):
    student.delete_one({'_id':ObjectId(id)})
    return redirect(url_for('index'))

    

if __name__ == '__main__':
    app.run(debug=True)
