from flask_restx import fields
from ..restx import api

payment_schema = api.model('Payment', {
    "CreditCardNumber": fields.String(required=True),
    "CardHolder": fields.String(required=True),
    "ExpirationDate": fields.DateTime(required=True),
    "SecurityCode": fields.String(),
    "Amount": fields.Float(required=True)
})