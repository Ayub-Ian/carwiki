from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel

class BidStatus(str, Enum):
    Accepted = "accepted"
    AcceptedBelowReserve = "accepted below reserve"
    TooLow = "too low"
    Finished = "finished"
    

class Auction(BaseModel):
    id: str
    auctionEnd: datetime 
    seller: str
    reservePrice: int
    finished: Optional[bool]

class Bid(BaseModel):
    auctionId: str
    bidder: str
    bidTime: datetime = datetime.now()
    amount: int
    bidStatus: BidStatus