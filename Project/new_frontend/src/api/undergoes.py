from flask_restful import Resource, request
from flask_login import login_required
from ..GLOBAL import DATABASE
from ..api import api_bp
import requests


@api_bp.route('/undergoess', methods=['POST'])
@login_required
def post_undergoess(self):
    response = requests.post(DATABASE + '/undergoess', json=request.get_json(force=True))
    return response


@api_bp.route('/undergoess', methods=['GET'])
@login_required
def get_undergoess(self):
    response = requests.get(DATABASE + '/undergoess')
    return response


@api_bp.route('/undergoes/<int:id>', methods=['GET'])
@login_required
def get_undergoes(self, id):
    response = requests.get(DATABASE + '/undergoes/' + str(id))
    return response


@api_bp.route('/undergoes/<int:id>', methods=['DELETE'])
@login_required
def delete_undergoes(self, id):
    response = requests.delete(DATABASE + '/undergoes/' + str(id))
    return response


@api_bp.route('/undergoes/<int:id>', methods=['PUT'])
@login_required
def put_undergoes(self, id):
    response = requests.put(DATABASE + '/undergoes/' + str(id),json=request.get_json(force=True))
    return response
