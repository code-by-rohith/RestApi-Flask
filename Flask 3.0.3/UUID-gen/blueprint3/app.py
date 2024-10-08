from flask import Flask
from operations.get import get_blueprint  
from operations.post import post_blueprint 
app = Flask(__name__)


app.register_blueprint(get_blueprint, url_prefix='/api') 
app.register_blueprint(post_blueprint, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True) 
