from flask import Blueprint, jsonify
from flask_restful import Resource, request
from flask_login import login_required
from ..GLOBAL import DATABASE
import requests

api_bp = Blueprint("api", __name__, url_prefix='/api')


# UnderGoes

@api_bp.route('/undergoes', methods=['POST'])
@login_required
def post_undergoess():
    response = requests.post(DATABASE + '/undergoes', json=request.get_json(force=True))
    return jsonify(response.json())


@api_bp.route('/undergoes', methods=['GET'])
@login_required
def get_undergoess():
    response = requests.get(DATABASE + '/undergoes')
    return jsonify(response.json())


@api_bp.route('/undergoes/<int:id>', methods=['GET'])
@login_required
def get_undergoes(id):
    response = requests.get(DATABASE + '/undergoes/' + str(id))
    return jsonify(response.json())


@api_bp.route('/undergoes/<int:id>', methods=['DELETE'])
@login_required
def delete_undergoes( id):
    response = requests.delete(DATABASE + '/undergoes/' + str(id))
    return jsonify(response.json())


@api_bp.route('/undergoes/<int:id>', methods=['PUT'])
@login_required
def put_undergoes( id):
    response = requests.put(DATABASE + '/undergoes/' + str(id), json=request.get_json(force=True))
    return jsonify(response.json())


# appointment

@api_bp.route('/appointment', methods=['POST'])
@login_required
def post_appointments():
    response = requests.post(DATABASE + '/appointment', json=request.get_json(force=True))
    return jsonify(response.json())


@api_bp.route('/appointment', methods=['GET'])
@login_required
def get_appointments():
    response = requests.get(DATABASE + '/appointment')
    return jsonify(response.json())


@api_bp.route('/appointment/<int:id>', methods=['GET'])
@login_required
def get_appointment(id):
    response = requests.get(DATABASE + '/appointment/' + str(id))
    return jsonify(response.json())


@api_bp.route('/appointment/<int:id>', methods=['PUT'])
@login_required
def put_appointment(id):
    response = requests.put(DATABASE + '/appointment/' + str(id), json=request.get_json(force=True))
    return jsonify(response.json())


# common

@api_bp.route('/common', methods=['GET'])
@login_required
def get_common():
    response = requests.get(DATABASE + '/common')
    return jsonify(response.json())


# department

@api_bp.route('/department', methods=['POST'])
@login_required
def post_departments():
    response = requests.post(DATABASE + '/department', json=request.get_json(force=True))
    return jsonify(response.json())


@api_bp.route('/department', methods=['GET'])
@login_required
def get_departments():
    response = requests.get(DATABASE + '/department')
    return jsonify(response.json())


@api_bp.route('/department/<int:id>', methods=['GET'])
@login_required
def get_department(id):
    response = requests.get(DATABASE + '/department/' + str(id))
    return jsonify(response.json())


@api_bp.route('/department/<int:id>', methods=['PUT'])
@login_required
def put_department( id):
    response = requests.put(DATABASE + '/department/' + str(id), json=request.get_json(force=True))
    return jsonify(response.json())


# doctor

@api_bp.route('/doctor', methods=['POST'])
@login_required
def post_doctors():
    response = requests.post(DATABASE + '/doctor', json=request.get_json(force=True))
    return jsonify(response.json())


@api_bp.route('/doctor', methods=['GET'])
@login_required
def get_doctors():
    response = requests.get(DATABASE + '/doctor')
    return jsonify(response.json())


@api_bp.route('/doctor/<int:id>', methods=['GET'])
@login_required
def get_doctor( id):
    response = requests.get(DATABASE + '/doctor/' + str(id))
    return jsonify(response.json())


@api_bp.route('/doctor/<int:id>', methods=['DELETE'])
@login_required
def delete_doctor( id):
    response = requests.delete(DATABASE + '/doctor/' + str(id))
    return jsonify(response.json())


@api_bp.route('/doctor/<int:id>', methods=['PUT'])
@login_required
def put_doctor( id):
    response = requests.put(DATABASE + '/doctor/' + str(id), json=request.get_json(force=True))
    return jsonify(response.json())


# medication

@api_bp.route('/medication', methods=['POST'])
@login_required
def post_medications():
    response = requests.post(DATABASE + '/medication', json=request.get_json(force=True))
    return jsonify(response.json())


@api_bp.route('/medication', methods=['GET'])
@login_required
def get_medications():
    response = requests.get(DATABASE + '/medication')
    return jsonify(response.json())


@api_bp.route('/medication/<int:id>', methods=['GET'])
@login_required
def get_medication(id):
    response = requests.get(DATABASE + '/medication/' + str(id))
    return jsonify(response.json())


@api_bp.route('/medication/<int:id>', methods=['DELETE'])
@login_required
def delete_medication(id):
    response = requests.delete(DATABASE + '/medication/' + str(id))
    return jsonify(response.json())


@api_bp.route('/medication/<int:id>', methods=['PUT'])
@login_required
def put_medication(id):
    response = requests.put(DATABASE + '/medication/' + str(id), json=request.get_json(force=True))
    return jsonify(response.json())


# nurse

@api_bp.route('/nurse', methods=['POST'])
@login_required
def post_nurses():
    response = requests.post(DATABASE + '/nurse', json=request.get_json(force=True))
    return jsonify(response.json())


@api_bp.route('/nurse', methods=['GET'])
@login_required
def get_nurses():
    response = requests.get(DATABASE + '/nurse')
    return jsonify(response.json())


@api_bp.route('/nurse/<int:id>', methods=['GET'])
@login_required
def get_nurse(id):
    response = requests.get(DATABASE + '/nurse/' + str(id))
    return jsonify(response.json())


@api_bp.route('/nurse/<int:id>', methods=['DELETE'])
@login_required
def delete_nurse( id):
    response = requests.delete(DATABASE + '/nurse/' + str(id))
    return jsonify(response.json())


@api_bp.route('/nurse/<int:id>', methods=['PUT'])
@login_required
def put_nurse( id):
    response = requests.put(DATABASE + '/nurse/' + str(id), json=request.get_json(force=True))
    return jsonify(response.json())


# patient

@api_bp.route('/patient', methods=['POST'])
@login_required
def post_patients():
    response = requests.post(DATABASE + '/patient', json=request.get_json(force=True))
    return jsonify(response.json())


@api_bp.route('/patient', methods=['GET'])
@login_required
def get_patients():
    response = requests.get(DATABASE + '/patient')
    return jsonify(response.json())


@api_bp.route('/patient/<int:id>', methods=['GET'])
@login_required
def get_patient(id):
    response = requests.get(DATABASE + '/patient/' + str(id))
    return jsonify(response.json())


@api_bp.route('/patient/<int:id>', methods=['DELETE'])
@login_required
def delete_patient(id):
    response = requests.delete(DATABASE + '/patient/' + str(id))
    return jsonify(response.json())


@api_bp.route('/patient/<int:id>', methods=['PUT'])
@login_required
def put_patient(id):
    response = requests.put(DATABASE + '/patient/' + str(id), json=request.get_json(force=True))
    return jsonify(response.json())


# prescribes

@api_bp.route('/prescribe', methods=['POST'])
@login_required
def post_prescribes():
    response = requests.post(DATABASE + '/prescribe', json=request.get_json(force=True))
    return jsonify(response.json())


@api_bp.route('/prescribe', methods=['GET'])
@login_required
def get_prescribes():
    response = requests.get(DATABASE + '/prescribe')
    return jsonify(response.json())


@api_bp.route('/prescribe/<int:id>', methods=['GET'])
@login_required
def get_prescribe(id):
    response = requests.get(DATABASE + '/prescribe/' + str(id))
    return jsonify(response.json())


@api_bp.route('/prescribe/<int:id>', methods=['DELETE'])
@login_required
def delete_prescribe(id):
    response = requests.delete(DATABASE + '/prescribe/' + str(id))
    return jsonify(response.json())


@api_bp.route('/prescribe/<int:id>', methods=['PUT'])
@login_required
def put_prescribe(id):
    response = requests.put(DATABASE + '/prescribe/' + str(id), json=request.get_json(force=True))
    return jsonify(response.json())


# procedure

@api_bp.route('/procedure', methods=['POST'])
@login_required
def post_procedures():
    response = requests.post(DATABASE + '/procedure', json=request.get_json(force=True))
    return jsonify(response.json())


@api_bp.route('/procedure', methods=['GET'])
@login_required
def get_procedures():
    response = requests.get(DATABASE + '/procedure')
    return jsonify(response.json())


@api_bp.route('/procedure/<int:id>', methods=['GET'])
@login_required
def get_procedure(id):
    response = requests.get(DATABASE + '/procedure/' + str(id))
    return jsonify(response.json())


@api_bp.route('/procedure/<int:id>', methods=['DELETE'])
@login_required
def delete_procedure(id):
    response = requests.delete(DATABASE + '/procedure/' + str(id))
    return jsonify(response.json())


@api_bp.route('/procedure/<int:id>', methods=['PUT'])
@login_required
def put_procedure(id):
    response = requests.put(DATABASE + '/procedure/' + str(id), json=request.get_json(force=True))
    return jsonify(response.json())


# room

@api_bp.route('/room', methods=['POST'])
@login_required
def post_rooms():
    response = requests.post(DATABASE + '/room', json=request.get_json(force=True))
    return jsonify(response.json())


@api_bp.route('/room', methods=['GET'])
@login_required
def get_rooms():
    response = requests.get(DATABASE + '/room')
    return jsonify(response.json())


@api_bp.route('/room/<int:id>', methods=['GET'])
@login_required
def get_room(id):
    response = requests.get(DATABASE + '/room/' + str(id))
    return jsonify(response.json())


@api_bp.route('/room/<int:id>', methods=['DELETE'])
@login_required
def delete_room(id):
    response = requests.delete(DATABASE + '/room/' + str(id))
    return jsonify(response.json())


@api_bp.route('/room/<int:id>', methods=['PUT'])
@login_required
def put_room(id):
    response = requests.put(DATABASE + '/room/' + str(id), json=request.get_json(force=True))
    return jsonify(response.json())
