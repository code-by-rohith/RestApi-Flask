from flask import Flask , Blueprint
from func.subapp import appsite


app =  Flask(__name__)

app.register_blueprint(appsite ,  url_prefix ='/api')


if __name__ == '__main__':
    app.run(debug= True)



