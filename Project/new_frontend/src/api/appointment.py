from flask_restful import Resource, request
from flask_login import login_required
from ..GLOBAL import DATABASE
from ..api import api_bp
import requests


@api_bp.route('/appointments', methods=['POST'])
@login_required
def post_appointments(self):
    response = requests.post(DATABASE + '/appointments', json=request.get_json(force=True))
    return response


@api_bp.route('/appointments', methods=['GET'])
@login_required
def get_appointments(self):
    response = requests.get(DATABASE + '/appointments')
    return response


@api_bp.route('/appointment/<int:id>', methods=['GET'])
@login_required
def get_appointment(self, id):
    response = requests.get(DATABASE + '/appointment/' + str(id))
    return response


@api_bp.route('/appointment/<int:id>', methods=['PUT'])
@login_required
def put_appointment(self, id):
    response = requests.put(DATABASE + '/appointment/' + str(id), json=request.get_json(force=True))
    return response
