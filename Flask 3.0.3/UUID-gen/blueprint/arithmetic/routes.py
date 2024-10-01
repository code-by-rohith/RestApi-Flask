from flask import jsonify
from . import arithmetic_bp

@arithmetic_bp.route('/calculate/<int:num1>/<int:num2>/<string:operation>', methods=['GET'])
def calculate(num1, num2, operation):
    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            result = num1 / num2
        else:
            return jsonify({"error": "Division by zero is not allowed."}), 400
    else:
        return jsonify({"error": "Invalid operation."}), 400

    return jsonify({"result": result})
