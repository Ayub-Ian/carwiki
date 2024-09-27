from flask_restful import Resource
from flask import request
from pymongo.collection import Collection
from app.models import Item

# from app import pymongo

from pymongo import MongoClient
client = MongoClient("mongodb://root:mongopw@localhost:27017/")
db = client["SearchDb"]

items: Collection = db.items



class SearchResource(Resource):
    def get(self):

        page = int(request.args.get("page", 1))
        per_page = 10  # A const value.

        cursor = items.find().sort("make").skip(per_page * (page - 1)).limit(per_page)

        items_count = items.count_documents({})
        return {
            "data": [Item(**doc).model_dump(mode='json') for doc in cursor],
            "pageCount": items_count,
        }, 200
