
from flask import Flask
from flask_restful import Api
from flasgger import Swagger

app = Flask(__name__)

app.config['SWAGGER'] = {
    'title': 'Chlorophyll API',
}
swagger = Swagger(app)

api = Api(app)