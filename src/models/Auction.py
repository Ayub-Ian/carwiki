import datetime
import enum
from typing import Optional

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()

class Status(enum.Enum):
    LIVE = "live"
    FINISHED = "finished"
    RESERVENOTMET = "reserve not met"



class Auction(db.Model):
    id: Mapped[int]
    reserved_price: Mapped[int]
    seller: Mapped[str]
    winner: Mapped[Optional[str]]
    sold_amount: Mapped[Optional[int]]
    current_high_bid: Mapped[Optional[int]]
    created_at: Mapped[datetime.datetime]
    updated_at: Mapped[datetime.datetime]
    auction_end: Mapped[datetime.datetime]
    status: Mapped[Status]
    item: Mapped[int]
