import inflection
from flask import request
from flask_restful import Resource

from app import db, manager
from app.models import Auction, Item


class AuctionResource(Resource):
    def get(self, auction_id):
        auction = db.session.get(Auction, {"id": auction_id})

        if not auction:
            return {"message": "No auction found with id."}, 404

        return {
                "id": auction.id,
                "createdAt": auction.created_at.isoformat(),
                "updatedAt": auction.updated_at.isoformat(),
                "auctionEnd": auction.auction_end.isoformat(),
                "seller": auction.seller,
                "winner": auction.winner,
                "make": auction.item.make,
                "model": auction.item.model,
                "year": auction.item.year,
                "color": auction.item.color,
                "mileage": auction.item.mileage,
                "imageUrl": auction.item.image_url,
                "status": auction.status.name,
                "reservePrice": auction.reserve_price,
                "soldAmount": auction.sold_amount,
                "currentHighBid": auction.current_high_bid
            }, 200 

class AuctionsResource(Resource):
    def get(self):
        auctions = Auction.query.all()
        return [
            {
                "id": auction.id,
                "createdAt": auction.created_at.isoformat(),
                "updatedAt": auction.updated_at.isoformat(),
                "auctionEnd": auction.auction_end.isoformat(),
                "seller": auction.seller,
                "winner": auction.winner,
                "make": auction.item.make,
                "model": auction.item.model,
                "year": auction.item.year,
                "color": auction.item.color,
                "mileage": auction.item.mileage,
                "imageUrl": auction.item.image_url,
                "status": auction.status.name,
                "reservePrice": auction.reserve_price,
                "soldAmount": auction.sold_amount,
                "currentHighBid": auction.current_high_bid
            } for auction in auctions
        ], 200

    def post(self):
        seller = "test"
        data = request.get_json()

        entities = {inflection.underscore(k):v for k,v in data.items()}

        auction = Auction(
            reserve_price = entities["reserve_price"],
            auction_end = entities["auction_end"],
            seller = seller,
            item = Item (
                image_url = entities["image_url"],
                mileage = entities["mileage"],
                model = entities["model"],
                make = entities["make"],
                color = entities["color"],
                year = entities["year"]
            )
        )

        try:
            db.session.add(auction)
            db.session.commit()

            manager.publish({
                "id": 120378
            }, "AuctionSvc.AuctionCreated", "auction_created")

            return {"message": f"successfully created auction {auction.id}"}
         
        except Exception as e:
            db.session.rollback()
            return {"message": str(e)}, 500
