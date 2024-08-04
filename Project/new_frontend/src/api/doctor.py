from flask_restful import Resource, request
from flask_login import login_required
from ..GLOBAL import DATABASE
from ..api import api_bp
import requests


@api_bp.route('/doctors', methods=['POST'])
@login_required
def post_doctors(self):
    response = requests.post(DATABASE + '/doctors', json=request.get_json(force=True))
    return response


@api_bp.route('/doctors', methods=['GET'])
@login_required
def get_doctors(self):
    response = requests.get(DATABASE + '/doctors')
    return response


@api_bp.route('/doctor/<int:id>', methods=['GET'])
@login_required
def get_doctor(self, id):
    response = requests.get(DATABASE + '/doctor/' + str(id))
    return response


@api_bp.route('/doctor/<int:id>', methods=['DELETE'])
@login_required
def delete_doctor(self, id):
    response = requests.delete(DATABASE + '/doctor/' + str(id))
    return response


@api_bp.route('/doctor/<int:id>', methods=['PUT'])
@login_required
def put_doctor(self, id):
    response = requests.put(DATABASE + '/doctor/' + str(id),json=request.get_json(force=True))
    return response
