from flask import Flask, redirect, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String, nullable=False)  
    roll_no = db.Column(db.Integer, nullable=False)  

    def __repr__(self):
        return f'<User {self.name}>'

@app.route('/')
def main():
    return "Welcome"

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        roll_no = request.form.get('roll_no')
        data = User(name=name, roll_no=roll_no)
        db.session.add(data)
        db.session.commit()
        return render_template('index.html', message="Inserted")
    return render_template('index.html', message="Error")  

if __name__ == "__main__":
    with app.app_context():  
        db.create_all()  
    app.run(debug=True)
