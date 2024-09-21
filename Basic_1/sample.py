from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/register')
def homepage():
    return render_template('register.html')

@app.route('/con', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        try:
            name = request.form.get('name')
            city = request.form.get('city')
            id = request.form.get('id')
            return render_template('final.html', name=name, city=city, id=id)
        except Exception as e:
            print(f"ERROR: {e}")
            return "An error occurred. Please try again."
    else:
        return render_template('register.html')


if __name__ == '__main__':
    app.run(port=900,debug=True)

