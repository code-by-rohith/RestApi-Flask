from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    orders = db.relationship('Order', backref='user', lazy=True)


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(120), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/add_data')
def add_data():    
    new_user = User(username='John Doe')
    db.session.add(new_user)
    db.session.commit()  
    order_1 = Order(product_name='Laptop', user_id=new_user.id)
    order_2 = Order(product_name='Smartphone', user_id=new_user.id)
    db.session.add_all([order_1, order_2])
    db.session.commit()  

    return "Test data added successfully!"

@app.route('/')
def index():
    users = User.query.all() 
    return render_template('index.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
