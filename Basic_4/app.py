from flask import Flask , request , render_template , url_for , redirect


app= Flask(__name__)

@app.route('/')
def home():
    return "<h1>HI<h1>"

@app.route('/fun')
def func():
    a=[1,2,3,4,5,6,7,8,9,10]
    return render_template('temp.html',func=a)
@app.route('/other')
def sample():
    word="This Is From Code By Rohith"
    return render_template('temp1.html',word=word)

@app.template_filter('reverse_string')
def reverse_string(s):
    return s[::-1]

@app.template_filter('upper1')
def upper(s):
    return s.upper()

@app.template_filter('repeat')
def repeat(s,times):
    return s*times

@app.template_filter('pattern')
def pattern(word):
    a=word.split()
    return a

@app.template_filter('replate')
def replate(word):
    return ''.join([c.upper() if i%2==0 else c.lower() for i , c in enumerate(word)])

@app.route('/go_home')
def go_home():
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(port=5000,debug=True)