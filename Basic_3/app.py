from flask import  Flask , render_template , request

app=Flask(__name__)

@app.route('/')
def main():
    return render_template('front.html')

@app.route('/leet',methods=['POST','GET'])
def homepage():
    if request.method=='POST':
        try:
            n=request.form.get('value')
            def internal(n):
                return n[::-1]

            return render_template('value.html',value=internal(n))
        except Exception as e:
            return f"Error{e}"
    else :
        return render_template('warning.html')


if __name__ =='__main__':
    app.run(debug=True)
