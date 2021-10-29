
from flask.blueprints import Blueprint
from flask import request
from flask.wrappers import Response

from .util import error_response

bp = Blueprint('handlers', __name__)

@bp.app_errorhandler(404)
def not_found(error) -> Response:
    return Response(error_response(f"URI \'{request.path}\' not found"), mimetype='application/json', status=404)

@bp.app_errorhandler(405)
def method_not_allowed(error) -> Response:
    return Response(
        error_response(f"The \'{request.method}\' method is not allowed at \'{request.path}\'."), 
        mimetype='application/json', 
        status=405
    )

@bp.app_errorhandler(400)
def bad_request(error) -> Response:
    return Response(
        error_response("Bad Request"),
        mimetype='application/json',
        status=400
    )

@bp.app_errorhandler(500)
def internal_server_error(error) -> Response:
    return Response(
        error_response("Internal Server Error"),
        mimetype='application/json',
        status=500
    )
