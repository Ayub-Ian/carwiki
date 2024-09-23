from flask_restful import Resource

from app.models import Auction

class AuctionResource(Resource):
    def get(self):
        auctions = Auction.query.all()
        return [
            {
                "id": auction.id,
                "CreatedAt": auction.created_at.isoformat(),
                "UpdatedAt": auction.updated_at.isoformat(),
                "AuctionEnd": auction.auction_end.isoformat(),
                "Seller": auction.seller,
                "Winner": auction.winner,
                "Make": auction.item.make,
                "Model": auction.item.model,
                "Year": auction.item.year,
                "Color": auction.item.color,
                "Mileage": auction.item.mileage,
                "ImageUrl": auction.item.image_url,
                "Status": auction.status.name,
                "ReservePrice": auction.reserve_price,
                "SoldAmount": auction.sold_amount,
                "CurrentHighBid": auction.current_high_bid
            } for auction in auctions
        ], 200
