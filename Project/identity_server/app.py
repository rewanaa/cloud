from flask import Flask
from flask_restful import Api
from package import Validate, Login
from package.GLOBAL import args

app = Flask(__name__, static_url_path='')
api = Api(app)
api.add_resource(Validate, '/validate')
api.add_resource(Login, '/login')

# Routes
if __name__ == '__main__':
    app.run(debug=True, host=args.host, port=args.port)
