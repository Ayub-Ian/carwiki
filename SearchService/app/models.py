from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

class Item(BaseModel):
    id: str
    createdAt: datetime
    updatedAt: datetime
    auctionEnd: datetime
    seller: str
    winner: Optional[str]
    make: str
    model: str
    year: int
    color: str
    mileage: int
    imageUrl: str
    status: str
    reservePrice: int
    soldAmount: Optional[int]
    currentHighBid: Optional[int]
