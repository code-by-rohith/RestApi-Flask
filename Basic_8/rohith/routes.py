from flask import Blueprint

welcome_function = Blueprint('rohith', __name__)

a = 66 

@welcome_function.route('/')
def rohith():
    return f'Welcome Rohith, value of a is {a}'  