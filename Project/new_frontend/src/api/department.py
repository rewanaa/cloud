from flask_restful import Resource, request
from flask_login import login_required
from ..GLOBAL import DATABASE
from ..api import api_bp
import requests


@api_bp.route('/departments', methods=['POST'])
@login_required
def post_departments(self):
    response = requests.post(DATABASE + '/departments', json=request.get_json(force=True))
    return response


@api_bp.route('/departments', methods=['GET'])
@login_required
def get_departments(self):
    response = requests.get(DATABASE + '/departments')
    return response


@api_bp.route('/department/<int:id>', methods=['GET'])
@login_required
def get_department(self, id):
    response = requests.get(DATABASE + '/department/' + str(id))
    return response


@api_bp.route('/department/<int:id>', methods=['PUT'])
@login_required
def put_department(self, id):
    response = requests.put(DATABASE + '/department/' + str(id),json=request.get_json(force=True))
    return response
