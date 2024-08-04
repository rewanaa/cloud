from argparse import ArgumentParser
parser = ArgumentParser()
parser.add_argument("-db", "--database", dest='database', default="database.db")
parser.add_argument("-p", "--port", dest='port', default="5000", type=int)
parser.add_argument("--host", dest='host', default="127.0.0.1")
parser.add_argument("--timeout", dest='timeout', default="300", type=int)
args = parser.parse_args()