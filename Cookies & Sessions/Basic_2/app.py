from flask import Flask, session, redirect, url_for, request, render_template

app = Flask(__name__)

# Secret key is required to use session (it can be any random string)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    if 'username' in session:
        return f"Logged in as {session['username']}"
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form.get('username')
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it exists
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
