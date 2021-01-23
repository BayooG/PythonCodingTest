from flask_restx import Api


api = Api()


@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    

# @api.errorhandler(Exception)
# def default_error_handler(e):
#     message = 'payment could not be proccessed.'
    

