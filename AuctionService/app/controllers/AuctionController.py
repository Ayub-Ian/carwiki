import inflection
from flask import request
from flask_restful import Resource

from app import db, manager
from app.models import Auction, Item
from schemas.AuctionSchema import AuctionSchema

auction_schema = AuctionSchema()

class AuctionResource(Resource):
    def get(self, auction_id):
        auction = db.session.get(Auction, {"id": auction_id})

        if not auction:
            return {"message": "No auction found with id."}, 404

        return auction_schema.dump(auction), 200 
    
    def put(self, auction_id):
        pass

    def delete(self, auction_id):
        auction = db.session.get(Auction, {"id": auction_id})


        try:
            db.session.delete(auction)
            db.session.commit()

            manager.publish({"id": auction_id}, "AuctionSvc.AuctionDeleted", "auction_deleted")

            return {"message": f"Deleted auction {auction_id}"}
         
        except Exception as e:
            db.session.rollback()
            return {"message": str(e)}, 500

      

class AuctionsResource(Resource):
    def get(self):
        auctions = Auction.query.all()
        return [
            auction_schema.dump(auction) for auction in auctions
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

            manager.publish(auction_schema.dump(auction), "AuctionSvc.AuctionCreated", "auction_created")

            return {"message": auction_schema.dump(auction)}
         
        except Exception as e:
            db.session.rollback()
            return {"message": str(e)}, 500
