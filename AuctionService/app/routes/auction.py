from flask import Blueprint
from flask_restful import Api

from app.controllers.AuctionController import AuctionResource

routes = Blueprint('auctions', __name__)

api = Api(routes)

api.add_resource(AuctionResource, '/auctions')
