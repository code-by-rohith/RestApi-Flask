from flask import  Flask , render_template , make_response,request

app= Flask(__name__)


@app.route('/cookies')
def main():
    res=request.cookies.get("Value")
    return f"<h1>Cookies is {res} <h1>"
@app.route('/')
def cookies():
    res= make_response("<h1>Cookies<h1>")
    res.set_cookie("Value","Black")
    return res


if __name__=='__main__':
    app.run(debug=True)