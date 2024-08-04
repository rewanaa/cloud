from flask_restful import Resource, request
from flask_login import login_required
from ..GLOBAL import DATABASE
from ..api import api_bp
import requests


@api_bp.route('/procedures', methods=['POST'])
@login_required
def post_procedures(self):
    response = requests.post(DATABASE + '/procedures', json=request.get_json(force=True))
    return response


@api_bp.route('/procedures', methods=['GET'])
@login_required
def get_procedures(self):
    response = requests.get(DATABASE + '/procedures')
    return response


@api_bp.route('/procedure/<int:id>', methods=['GET'])
@login_required
def get_procedure(self, id):
    response = requests.get(DATABASE + '/procedure/' + str(id))
    return response


@api_bp.route('/procedure/<int:id>', methods=['DELETE'])
@login_required
def delete_procedure(self, id):
    response = requests.delete(DATABASE + '/procedure/' + str(id))
    return response


@api_bp.route('/procedure/<int:id>', methods=['PUT'])
@login_required
def put_procedure(self, id):
    response = requests.put(DATABASE + '/procedure/' + str(id),json=request.get_json(force=True))
    return response
