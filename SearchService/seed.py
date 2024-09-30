import json
from pymongo import MongoClient, ASCENDING
from pymongo.errors import ConnectionFailure, BulkWriteError
from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional, List
import os
from app.models import Item

# class Item(BaseModel):
#     id: str = Field(alias="_id")
#     createdAt: datetime
#     updatedAt: datetime
#     auctionEnd: datetime
#     seller: str
#     winner: Optional[str]
#     make: str
#     model: str
#     year: int
#     color: str
#     mileage: int
#     imageUrl: str
#     status: str
#     reservePrice: int
#     soldAmount: Optional[int]
#     currentHighBid: Optional[int]


# MongoDB connection setup
def connect_to_mongo(uri: str, db_name: str):
    try:
        client = MongoClient(uri)
        # Trigger a command to ensure connection is successful
        client.admin.command('ping')
        db = client[db_name]
        print("Successfully connected to MongoDB")
        return db
    except ConnectionFailure as e:
        print(f"MongoDB connection failed: {e}")
        return None

# Function to create indexes
def create_indexes(collection):
    try:
        collection.create_index([('make', 'text'), ('color', 'text'), ('model', 'text')])
        print("Indexes on 'Make', 'Color', and 'Model' created!")
    except Exception as e:
        print(f"Failed to create indexes: {e}")

# Function to load data from JSON file
def load_data_from_json(file_path: str) -> List[Item]:
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        # Parse each JSON object into Pydantic models
        items = [Item(**item) for item in data]
        print(items)
        print(f"Loaded {len(items)} items from JSON file.")
        return items
    except FileNotFoundError as e:
        print(f"File not found: {e}")
        return []
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON file: {e}")
        return []

# Function to check if collection is empty and seed data
def seed_data(collection, file_path: str):
    try:
        collection.delete_many({})

        if collection.count_documents({}) == 0:
            print("No data found in collection, seeding data...")
            items = load_data_from_json(file_path)
            if items:
                collection.insert_many([item.dict(by_alias=True) for item in items])
                print("Seed data inserted!")
            else:
                print("No valid data to insert.")
        else:
            print("Collection already has data. No action taken.")
    except BulkWriteError as e:
        print(f"Error inserting seed data: {e.details}")
    except Exception as e:
        print(f"Unexpected error during seeding: {e}")

# Main script execution
if __name__ == "__main__":
    # MongoDB URI and database name
    MONGO_URI = "mongodb://root:mongopw@localhost:27017/"
    DB_NAME = "SearchDb"

    # Connect to MongoDB
    db = connect_to_mongo(MONGO_URI, DB_NAME)

    if db is not None:
        collection = db['items']
        create_indexes(collection)

        # Path to seed data JSON file
        file_path = os.path.join(os.path.dirname(__file__), 'data','auctions.json')
        seed_data(collection, file_path)
