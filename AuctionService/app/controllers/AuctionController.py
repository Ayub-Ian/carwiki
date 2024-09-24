from flask_restful import Resource

from app.models import Auction

class AuctionResource(Resource):
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
