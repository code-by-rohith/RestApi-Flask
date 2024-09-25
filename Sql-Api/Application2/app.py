from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    roll_no = db.Column(db.Integer, unique=True)
    science = db.Column(db.Float)
    social = db.Column(db.Float)
    maths = db.Column(db.Float)
    percentage = db.Column(db.Float)

    def __repr__(self):
        return f'<User {self.name}>'
       
@app.route('/')
def home():
    return "Welcome to the website"

@app.route('/path', methods=['GET', 'POST'])
def data_valid():
    if request.method == 'POST':
        name = request.json.get('name')
        roll_no = request.json.get('roll_no')
        science = request.json.get('science')
        social = request.json.get('social')
        maths = request.json.get('maths')
        percentage = (science + social + maths) / 3
        new_data = User(
            name=name,
            roll_no=roll_no,
            science=science,
            social=social,
            maths=maths,
            percentage=percentage
        )
        db.session.add(new_data)
        db.session.commit()
        
        return jsonify({
            "id": new_data.id,
            "name": name,
            "roll_no": roll_no,
            "Science": science,
            "Social": social,
            "Maths": maths,
            "Percentage": percentage

        },{"message":"Sucessfully Added !!1 The Above Data"})
    
    return jsonify({"error": "Invalid method. Use POST."}), 405

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
