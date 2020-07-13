from app import create_app
from config import config
from flask import request, Blueprint
from flask_restful import Api
from flask_cors import CORS

from app.link import routes as routes_link

app = create_app(config['development'])

# BLUEPRINT
api_bp = Blueprint('api', __name__, url_prefix='/api/v1')

apiV1 = Api(api_bp)

app.register_blueprint(api_bp)

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

# ROUTES
routes_link(api=apiV1)

# SET DATABASE AND CACHE HERE

if __name__ == '__main__':
    app.run(host='0.0.0.0')
