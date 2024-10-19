from flask import Flask 
from flask import jsonify
from flask_restful import Api , Resource

app = Flask(__name__)
api = Api(app)

class Adding(Resource):
    def get(self):
        return "Welcome to the api"
    
api.add_resource(Adding ,'/api')


if __name__ == '__main__':
    app.run(debug= True)