from flask import Flask
from struct1.app import appbase


app= Flask(__name__)

app.register_blueprint(appbase,url_prefix='/get')


if __name__ == '__main__':
    app.run(debug=True)
