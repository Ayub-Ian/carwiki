from flask import Blueprint
from flask_restful import Api

from app.controllers.SearchController import SearchResource

routes = Blueprint('search', __name__)

api = Api(routes)

api.add_resource(SearchResource, '/search')
