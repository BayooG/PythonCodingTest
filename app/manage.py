from __future__ import absolute_import
import logging

from flask import Flask, Blueprint
from flask_script import Server, Manager

from app.api.restx import api
from app.api.v1.endpoints.payment import ns as payment_ns




application = Flask('Python Coding Test')
blueprint = Blueprint('api', __name__, url_prefix='/api/v1/')
api.init_app(blueprint)
api.add_namespace(payment_ns)
application.register_blueprint(blueprint)
manager = Manager(application)
manager.add_command("debug", Server(port=5000, use_debugger=True, host='0.0.0.0'))
manager.add_command("run", Server(port=5000, host='0.0.0.0'))



if __name__ == "__main__":
    application.logger.setLevel(logging.DEBUG)
    application.run(debug= True)

