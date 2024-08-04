import flask
from flask_restful import Resource, request
from .model import conn
from .token_generator import generate_token, hash_password
from datetime import datetime


class Login(Resource):
    def __init__(self):
        super().__init__()

    def post(self):
        user_data = request.get_json(force=True)
        user = conn.execute('''Select * FROM user WHERE email = ? and password = ?''', (user_data['email'],
                                                                                        hash_password(
                                                                                            user_data['password']))) \
            .fetchall()
        if len(user) == 1:
            token = generate_token(length=128)
            conn.execute('''INSERT INTO session(sess_token, user_id, sess_date) VALUES(?,?,?)''',
                         (token, user[0]['user_id'], datetime.now()))
            conn.commit()
            return {'token': token}
        else:
            return {'message': 'Email or password is incorrect'}, 403
