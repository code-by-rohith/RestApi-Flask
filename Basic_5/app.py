from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

users = {
    "Roh": "Roh",
    "vik":"vik"
}

@app.route('/sik', methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        return render_template('temp.html')
    elif request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        if users.get(name) == password:
            return '<h1>Success</h1>'
        else:
            return '<h1>Failed</h1>'

@app.route('/upload_file', methods=['POST'])
def upload_file():
    file = request.files['file']
    try:
        if file and file.filename:
            if file.filename.endswith('.txt'):
                return file.read().decode()
            elif file.filename.endswith(('.xlsx', '.xls', '.csv')):
                df = pd.read_excel(file) if file.filename.endswith(('.xlsx', '.xls')) else pd.read_csv(file)
                return df.to_html()
        return '<h1>No file uploaded or invalid file</h1>'
    except Exception as e:
        return f'<h1>Error: {e}</h1>'

if __name__ == '__main__':
    app.run(debug=True)
