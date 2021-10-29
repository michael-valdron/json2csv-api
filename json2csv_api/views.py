from json.decoder import JSONDecodeError
from flask import request
from flask.blueprints import Blueprint
from flask.wrappers import Response
from .models import Json, Csv
from .util import error_response

bp = Blueprint('views', __name__)

@bp.route('/v1/convert', methods=['POST'])
def convert() -> Response:
    try:
        in_data = Json.parse(request.data)
        if in_data.validate():
            out_data = Csv(in_data)
            return Response(out_data.write(), mimetype='text/csv', status=200)
        else:
            return Response(error_response("Form of JSON is invalid for conversion."), mimetype='application/json', status=400)
    except JSONDecodeError as e:
        return Response(error_response(e.msg), mimetype='application/json', status=400)        
