from flask import Flask, jsonify, request
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}
    def post(self):
        print (request.json['text'])
        return {'hello': 'world'}


api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)