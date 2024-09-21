from flask import Flask
from rohith.routes import welcome_function, a  # Import a from routes.py

app = Flask(__name__)

app.register_blueprint(welcome_function, url_prefix='/rohith')

@app.route('/')
def home():
    return f"ScreEN 1 {a}"  # Use the variable a from routes.py

if __name__ == '__main__':
    app.run(debug=True)
