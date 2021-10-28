from flask import json
from flask.blueprints import Blueprint
from flask.wrappers import Response

bp = Blueprint('views', __name__)

@bp.route('/v1/convert', methods=['POST'])
def convert() -> Response:
    return Response(json.dumps({}), mimetype='application/json', status=200)
