from flask_restful import Resource, request
from flask_login import login_required
from ..GLOBAL import DATABASE, IDENTITY_SERVER
from ..api import api_bp
import requests


@api_bp.route('/patients', methods=['POST'])
@login_required
def post_patients(self):
    response = requests.post(DATABASE + '/patients', json=request.get_json(force=True))
    return response


@api_bp.route('/patients', methods=['GET'])
@login_required
def get_patients(self):
    response = requests.get(DATABASE + '/patients')
    return response


@api_bp.route('/patient/<int:id>', methods=['GET'])
@login_required
def get_patient(self, id):
    response = requests.get(DATABASE + '/patient/' + str(id))
    return response


@api_bp.route('/patient/<int:id>', methods=['DELETE'])
@login_required
def delete_patient(self, id):
    response = requests.delete(DATABASE + '/patient/' + str(id))
    return response


@api_bp.route('/patient/<int:id>', methods=['PUT'])
@login_required
def put_patient(self, id):
    response = requests.put(DATABASE + '/patient/' + str(id),json=request.get_json(force=True))
    return response
