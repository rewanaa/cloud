from flask_restful import Resource, request
from flask_login import login_required
from ..GLOBAL import DATABASE, IDENTITY_SERVER
from ..api import api_bp
import requests


@api_bp.route('/prescribes', methods=['POST'])
@login_required
def post_prescribes(self):
    response = requests.post(DATABASE + '/prescribes', json=request.get_json(force=True))
    return response


@api_bp.route('/prescribes', methods=['GET'])
@login_required
def get_prescribes(self):
    response = requests.get(DATABASE + '/prescribes')
    return response


@api_bp.route('/prescribe/<int:id>', methods=['GET'])
@login_required
def get_prescribe(self, id):
    response = requests.get(DATABASE + '/prescribe/' + str(id))
    return response


@api_bp.route('/prescribe/<int:id>', methods=['DELETE'])
@login_required
def delete_prescribe(self, id):
    response = requests.delete(DATABASE + '/prescribe/' + str(id))
    return response


@api_bp.route('/prescribe/<int:id>', methods=['PUT'])
@login_required
def put_prescribe(self, id):
    response = requests.put(DATABASE + '/prescribe/' + str(id),json=request.get_json(force=True))
    return response
