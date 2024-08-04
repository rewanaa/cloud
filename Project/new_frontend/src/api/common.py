from flask_restful import Resource
from frontend.package.model import conn
from ..api import api_bp
import requests
from ..GLOBAL import DATABASE
from flask_login import login_required

@api_bp.route('/common', methods=['GET'])
@login_required
def get_common(self):
    response = requests.get(DATABASE + '/common')
    return response

