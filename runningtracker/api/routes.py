from flask import Blueprint

API_VERSION = 0
api = Blueprint('api', __name__, url_prefix=f'/api/v{API_VERSION}')


@api.route('/heartbeat')
def api_heartbeat():
    return 204, ''
