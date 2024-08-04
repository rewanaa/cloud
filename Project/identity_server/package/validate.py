from flask_restful import Resource, request
from flask import jsonify
from .model import conn
from datetime import datetime
from .GLOBAL import args


class Validate(Resource):
    def __init__(self):
        super().__init__()

    def delete_session(self, token):

        conn.execute('''DELETE FROM session WHERE sess_token=\"''' + token + '\"')
        conn.commit()

    def post(self):
        token = request.get_json(force=True)
        session = conn.execute("Select * FROM session WHERE \"sess_token\"= \"" + token['token'] + "\"") \
            .fetchall()

        if len(session) == 0:
            return {'message': 'session token is not valid'}, 401
        else:
            difference = datetime.now() - datetime.strptime(session[0]['sess_date'], "%Y-%m-%d %H:%M:%S.%f")
            if difference.total_seconds() > args.timeout:
                self.delete_session(token['token'])
                return {'message': 'session token has expired'}, 401
            return {'message': 'session token is valid'}, 200
