from flask import Flask , request , render_template
from pymongo import MongoClient

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('temp.html')



if __name__ == '__main__':
    app.run(debug=True)
