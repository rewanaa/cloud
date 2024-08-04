from flask_restful import Resource, request
from flask_login import login_required
from ..GLOBAL import DATABASE, IDENTITY_SERVER
from ..api import api_bp
import requests


@api_bp.route('/nurses', methods=['POST'])
@login_required
def post_nurses(self):
    response = requests.post(DATABASE + '/nurses', json=request.get_json(force=True))
    return response


@api_bp.route('/nurses', methods=['GET'])
@login_required
def get_nurses(self):
    response = requests.get(DATABASE + '/nurses')
    return response


@api_bp.route('/nurse/<int:id>', methods=['GET'])
@login_required
def get_nurse(self, id):
    response = requests.get(DATABASE + '/nurse/' + str(id))
    return response


@api_bp.route('/nurse/<int:id>', methods=['DELETE'])
@login_required
def delete_nurse(self, id):
    response = requests.delete(DATABASE + '/nurse/' + str(id))
    return response


@api_bp.route('/nurse/<int:id>', methods=['PUT'])
@login_required
def put_nurse(self, id):
    response = requests.put(DATABASE + '/nurse/' + str(id),json=request.get_json(force=True))
    return response
