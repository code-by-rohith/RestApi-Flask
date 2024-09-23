from flask import  Flask , session , request
from flask_session import Session



app=Flask(__name__)
app.secret_key="aeiou"

@app.route('/')
def main():
    session['Key']="Plan B"
    return "<h1>Session Made<h1>"


@app.route('/session')
def session_getter():
    cok= session.get('Key', None)
    return f"<h1>The message is {cok}<h1>"

if __name__ == "__main__":
    app.run(debug=True)