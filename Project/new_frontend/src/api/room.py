from flask_restful import Resource, request
from flask_login import login_required
from ..GLOBAL import DATABASE
from ..api import api_bp
import requests


@api_bp.route('/rooms', methods=['POST'])
@login_required
def post_rooms(self):
    response = requests.post(DATABASE + '/rooms', json=request.get_json(force=True))
    return response


@api_bp.route('/rooms', methods=['GET'])
@login_required
def get_rooms(self):
    response = requests.get(DATABASE + '/rooms')
    return response


@api_bp.route('/room/<int:id>', methods=['GET'])
@login_required
def get_room(self, id):
    response = requests.get(DATABASE + '/room/' + str(id))
    return response


@api_bp.route('/room/<int:id>', methods=['DELETE'])
@login_required
def delete_room(self, id):
    response = requests.delete(DATABASE + '/room/' + str(id))
    return response


@api_bp.route('/room/<int:id>', methods=['PUT'])
@login_required
def put_room(self, id):
    response = requests.put(DATABASE + '/room/' + str(id),json=request.get_json(force=True))
    return response
