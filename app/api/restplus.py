"""Bootstraps Restplus API"""

import os
import logging
import traceback

from flask import url_for 
from flask_restx import Api, apidoc, fields, reqparse 
from ..__version__ import __version__
from ..config import AppConfig

_logger = logging.getLogger(__name__)

API = Api(
    version=__version__,
    title='TODO API',
    description='TODO API provides resources for a TODO list.'
)

@API.errorhandler
def default_error_handler(e):
    """
    Logs all uncaught exceptions
    """

    message = 'An unhandled exception occurred.'
    _logger.exception(message)
    return {'message': message}, 500

def register_swagger(app, server_base):
    """
    Registers Swagger docs to be accessible from non root server base.
    For example https://localhost:5000/todoapp/api/v1, where /todoapp is server
    base in this example and is behind a reverse proxy. Please note that the
    function is safe to call even with standard

    Args:
        app: FLASK application instance
        server_base: non root server base
    """
    if server_base is not None and server_base != "":
        custom_apidoc = apidoc.Apidoc(
            'restplus_custom_doc',
            __name__,
            template_folder='templates',
            static_folder=os.path.dirname(apidoc.__file__) + '/static',
            static_url_path='/swaggerui'
        )
    else:
        # There is nothing to do as we are serving from root
        return

    @custom_apidoc.add_app_template_global
    def swagger_static(filename):
        url = url_for('restplus_custom_doc.static', filename=filename)
        return url

    _logger.info("Setting swagger assets to be served from %s", server_base)
    app.register_blueprint(custom_apidoc, url_prefix=server_base)