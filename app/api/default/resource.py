"""
Modules that provides Healthz namespace REST resources
"""
from http import HTTPStatus
from flask_restx import Resource, abort

from ..restplus import API

def register_namespace():
    """
    Initialises default namespace resources.
    """

    @API.route('/healthz')
    @API.response(HTTPStatus.OK, 'Flask App is ready to receive requests.')
    @API.response(HTTPStatus.INTERNAL_SERVER_ERROR, 'Flask App is no longer running.')
    class Healthz(Resource):
        """
        Resource used by Kubernetes probing
        """
        def get(self):
            ok = self._health()
            if ok:
                return HTTPStatus.OK
            else:
                return API.abort(code=HTTPStatus.BAD_REQUEST, message='Internal server error')

        def _health(self):
            return True