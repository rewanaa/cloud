from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-p", "--port", dest='port', default="5000", type=int)
parser.add_argument("--host", dest='host', default="127.0.0.1")
parser.add_argument("--identity_server", dest="identity_server", default="http://127.0.0.1:5000")
parser.add_argument("--database", dest="database", default="http://127.0.0.1:5001")
parser.add_argument("--secret_key", dest="secret_key", default="fdkjshfhjsdfdskfdsfdcbsjdkfdsdf")
args = parser.parse_args()


SECRET_KEY = args.secret_key
IDENTITY_SERVER = args.identity_server
DATABASE = args.database
HOST = args.host
PORT = args.port
