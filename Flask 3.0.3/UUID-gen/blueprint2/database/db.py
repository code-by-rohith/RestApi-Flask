from flask import Blueprint

tamper= Blueprint('tamper',__name__)

@tamper.route('/db')
def home():
    return "Data base Loaded"