from flask import Flask , request, render_template


app= Flask(__name__)
@app.route('/')
def front():
    return "welcome"

@app.route('/names/<name>/<year>')
def home(name,year):
    courses=["maths","science","social","biology","physics"]
    return render_template('ems.html',user_name=name,courses=courses,year=year)

@app.route('/sum/<int:number1>/<int:number2>')
def sumof(number1,number2):
    sum=number1+number2
    return f'{number1}+{number2}={sum}',404


@app.route('/loop/<int:write>')
def loop(write):
    num=[i for i in range(write)]
    return render_template('loop.html',num=num)




if __name__ =='__main__':
    app.run(debug=True)