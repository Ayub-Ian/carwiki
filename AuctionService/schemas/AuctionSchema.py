from marshmallow import Schema, fields
from datetime import datetime

class AuctionSchema(Schema):
    id = fields.Str()
    createdAt = fields.Method("get_created_at")
    updatedAt = fields.Method("get_updated_at")
    auctionEnd = fields.Method("get_auction_end")
    seller = fields.Str()
    winner = fields.Str()
    make = fields.Method("get_item_make")
    model = fields.Method("get_item_model")
    year = fields.Method("get_item_year")
    color = fields.Method("get_item_color")
    mileage = fields.Method("get_item_mileage")
    imageUrl = fields.Method("get_item_image_url")
    status = fields.Method("get_auction_status")
    reservePrice = fields.Float()
    soldAmount = fields.Float()
    currentHighBid = fields.Float()

    def get_created_at(self, auction):
        return auction.created_at.isoformat()

    def get_updated_at(self, auction):
        return auction.updated_at.isoformat()

    def get_auction_end(self, auction):
        return auction.auction_end.isoformat()

    def get_item_make(self, auction):
        return auction.item.make

    def get_item_model(self, auction):
        return auction.item.model

    def get_item_year(self, auction):
        return auction.item.year

    def get_item_color(self, auction):
        return auction.item.color

    def get_item_mileage(self, auction):
        return auction.item.mileage

    def get_item_image_url(self, auction):
        return auction.item.image_url
    
    def get_auction_status(self, auction):
        return auction.status.name