from flask import Flask
from arithmetic import arithmetic_bp

app = Flask(__name__)
app.register_blueprint(arithmetic_bp, url_prefix='/arithmetic')

if __name__ == '__main__':
    app.run(debug=True)
