from flask import Flask
from app.student_routes import student_bp

app = Flask(__name__)

app.register_blueprint(student_bp, url_prefix='/students')  

if __name__ == '__main__':
    app.run(debug=True) 
