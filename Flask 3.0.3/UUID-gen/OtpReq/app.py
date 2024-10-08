from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_mail import Mail, Message
import random
import os
from dotenv import load_dotenv

load_dotenv()  

app = Flask(__name__)
app.secret_key = 'your_swdwdwdwdwdecret_key'  


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587  
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
mail = Mail(app)

otp_storage = {}

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/send_otp', methods=['POST'])
def send_otp():
    email = request.form['email']

    if not email.endswith('@gmail.com'):
        flash('Please enter a valid Gmail address.', 'danger')
        return redirect(url_for('home'))

    otp = random.randint(100000, 999999)  
    otp_storage[email] = otp

    msg = Message('This Is A Automated Mail Generted By Flask_Mail ----By A MCA Guy ', sender=os.environ.get('MAIL_USERNAME'), recipients=[email])
    msg.body = f'Your OTP code is: {otp}'
    mail.send(msg)

    session['email'] = email 
    flash('OTP sent to your email!', 'info')
    return redirect(url_for('verify_otp'))

@app.route('/verify_otp', methods=['GET', 'POST'])
def verify_otp():
    if request.method == 'POST':
        entered_otp = request.form['otp']
        email = session.get('email')

        if email in otp_storage and otp_storage[email] == int(entered_otp):
            flash('OTP verified! You are logged in.', 'success')
            del otp_storage[email]  # Remove OTP after verification
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid OTP. Please try again.', 'danger')

    return render_template('verify.html')

@app.route('/dashboard')
def dashboard():
    return "Welcome to your dashboard!"

if __name__ == '__main__':
    app.run(debug=True)
