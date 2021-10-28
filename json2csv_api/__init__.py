from flask import Flask, json
from flask.wrappers import Response
from . import views

def create_app(test_config=None) -> Flask:
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev'
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    # register blueprints
    app.register_blueprint(views.bp)

    # index route
    @app.route('/', methods=['GET'])
    def index() -> Response:
        return Response(json.dumps({'body': {'message': 'Hello World!'}}), mimetype='application/json', status=200)

    return app
