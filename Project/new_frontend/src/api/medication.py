from flask_restful import Resource, request
from flask_login import login_required
from ..GLOBAL import DATABASE, IDENTITY_SERVER
from ..api import api_bp
import requests


@api_bp.route('/medications', methods=['POST'])
@login_required
def post_medications(self):
    response = requests.post(DATABASE + '/medications', json=request.get_json(force=True))
    return response


@api_bp.route('/medications', methods=['GET'])
@login_required
def get_medications(self):
    response = requests.get(DATABASE + '/medications')
    return response


@api_bp.route('/medication/<int:id>', methods=['GET'])
@login_required
def get_medication(self, id):
    response = requests.get(DATABASE + '/medication/' + str(id))
    return response


@api_bp.route('/medication/<int:id>', methods=['DELETE'])
@login_required
def delete_medication(self, id):
    response = requests.delete(DATABASE + '/medication/' + str(id))
    return response


@api_bp.route('/medication/<int:id>', methods=['PUT'])
@login_required
def put_medication(self, id):
    response = requests.put(DATABASE + '/medication/' + str(id),json=request.get_json(force=True))
    return response
