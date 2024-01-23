from flask import Blueprint, request

# define blueprint
endpoint_demo_bp = Blueprint('endpoint_demo', __name__)

# define endpoints
@endpoint_demo_bp.route('/demo/print', methods=['GET'])
def print_demo():
    return 'Hello, Blueprint!'

@endpoint_demo_bp.route('/demo/print_values', methods=['GET'])
def print_values():
    value = request.args.get('value')
    return value
    