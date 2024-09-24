from flask import Blueprint
from flask_restful import Api

from app.controllers.AuctionController import AuctionResource, AuctionsResource

routes = Blueprint('auctions', __name__)

api = Api(routes)

api.add_resource(AuctionsResource, '/auctions')
api.add_resource(AuctionResource, '/auctions/<string:auction_id>')