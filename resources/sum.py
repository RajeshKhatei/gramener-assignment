from flask_restful import Resource
from flask import request


class SumAPI(Resource):

    def get(self):
        try:
            num1 = request.args.get('num1', None)
            num2 = request.args.get('num2', None)

            if num1 is None:
                return {'status': False, 'msg': 'Number required'}, 400

            if num2 is None:
                return {'status': False, 'msg': 'Number required'}, 400

            response = {
                           'status': True,
                           'value': (int(num1) + int(num2))
                       }, 200

            return response
        except Exception as e:
            return {'status': False, 'msg': str(e)}, 500
