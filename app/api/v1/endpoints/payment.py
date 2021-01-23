from flask import request
from app.api.restx import api
from app.api.v1.serializers import payment_schema as payment
from app.api.v1.business import ProcessPayment
from app.api.v1.validators import validate_payment
from flask_restx import Resource


ns = api.namespace('payment', path='/payment')

@ns.route('')
class PaymentCollection(Resource):
    
    @api.expect(payment)
    @api.response(200,'Ok')
    @api.response(400,'Bad Request')
    @api.response(500,'Internal Server Error')
    def post(self):
        data = request.json
        if validate_payment(data):
            ProcessPayment(data)
            return {'message': 'Payment is processed'}, 200
        else:
            return {'message': 'The request is invalid'}, 400
        