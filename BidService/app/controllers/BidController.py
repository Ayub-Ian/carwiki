
from datetime import datetime
from flask_restful import Resource
from flask import request
from pymongo.collection import Collection
from app.models import Bid, BidStatus
from pymongo import AsyncMongoClient, DESCENDING

client = AsyncMongoClient("mongodb://root:mongopw@localhost:27017/").aconnect()
db = client["BidsDb"]

auctions: Collection = db.auctions
bids: Collection = db.bids



class BidsResource(Resource):

    async def post(self):
        
        data = request.get_json()
        auctionId, amount, user = data
        
        auction = await auctions.find_one({"id": auctionId})
        
        if not auction:
            # TODO: check with auction service if has auction
            return {"message": "Auction does not exist"}, 404
        
        if auction.seller == user:
            return {"message": "Cannot bid on own auction"}, 409
        
        bid = Bid(auctionId=auctionId,
                  amount=amount,
                  bidder=user,
        )
        
        if auction.auctionEnd < datetime.now():
            bid.bidStatus = BidStatus.Finished
        else:
                
            highBid = await bids.find({"id": data.auctionId}).sort('amount',DESCENDING).limit(1)
            
            if highBid and amount > highBid.amount or not highBid:
                bid.bidStatus = BidStatus.Accepted if amount > auction.reservePrice else BidStatus.AcceptedBelowReserve 
                
            if highBid and bid.amount <= highBid.amount:
                bid.bidStatus = BidStatus.TooLow
                
        await bids.insert_one(bid.model_dump(mode='json'))
        
        return bid.model_dump(mode='json'), 200


class BidResource(Resource):
    
    async def get(self, auctionId):
        
        bid = await bids.find_one({"auctionId": auctionId }).sort('bidTime', DESCENDING)
        
        return Bid(**bid).model_dump_json()
        