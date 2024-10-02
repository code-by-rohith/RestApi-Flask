from flask import Flask , Blueprint 
from database.db import tamper


app= Flask(__name__)
app.register_blueprint(tamper,url_prefix='/data')





if __name__ == '__main__':
    app.run(debug=True)
