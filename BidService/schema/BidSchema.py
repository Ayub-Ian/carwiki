from datetime import datetime
from pydantic import BaseModel, Field



class Bid(BaseModel):
    id: str = Field(serialization_alias="_id")
    auctionId: str
    bidder: str
    bidTime: datetime
    amount: int
    bidStatus: str