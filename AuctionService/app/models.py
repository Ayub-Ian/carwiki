from datetime import datetime
import enum
import uuid
from app import db

class Status(enum.Enum):
    LIVE = "live"
    FINISHED = "finished"
    RESERVE_NOT_MET = "ReserveNotMet"



class Auction(db.Model):
    __tablename__ = 'auctions'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))  # GUID
    reserve_price = db.Column(db.Integer, default=0)
    seller = db.Column(db.String(100), nullable=False)  # Username from claim
    winner = db.Column(db.String(100), nullable=True)  # Username of winner
    sold_amount = db.Column(db.Integer, nullable=True)  # Optional
    current_high_bid = db.Column(db.Integer, nullable=True)  # Optional
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Default to UTC
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    auction_end = db.Column(db.DateTime, nullable=False)  # Must specify
    status = db.Column(db.Enum(Status), default=Status.LIVE)  # Enum for status
    item_id = db.Column(db.String, db.ForeignKey('items.id',ondelete='CASCADE'), nullable=False)  # Foreign key to Item

    # Relationship to Item model
    item = db.relationship('Item', back_populates="auction")

    # def to_dict(self):
    #     return {
    #         "id": self.id,
    #         "status": self.status.value,  # Convert Enum to string
    #         "reserve_price": self.reserve_price,
    #         "seller": self.seller,
    #         }

class Item(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))  # Primary key
    make = db.Column(db.String(100), nullable=False)  # Item make
    model = db.Column(db.String(100), nullable=False)  # Item model
    year = db.Column(db.Integer, nullable=False)  # Manufacturing year
    color = db.Column(db.String(50), nullable=False)  # Item color
    mileage = db.Column(db.Integer, nullable=False)  # Mileage of the item
    image_url = db.Column(db.String(255), nullable=True)  # Optional image URL
    auction = db.relationship('Auction', back_populates="item")  # One-to-one with Auction
