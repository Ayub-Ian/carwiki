from flask_restful import Resource
from flask import request
from pymongo.collection import Collection
from app.models import Item

from app import pymongo

items: Collection = pymongo.db.items


class SearchResource(Resource):
    def get(self):

        page = int(request.args.get("page", 1))
        per_page = 10  # A const value.

        cursor = items.find().sort("make").skip(per_page * (page - 1)).limit(per_page)

        items_count = items.count_documents({})
        return {
            "recipes": [Item(**doc).to_json() for doc in cursor],
            "pageCount": per_page,
        }, 200
