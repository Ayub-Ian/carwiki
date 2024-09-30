
from datetime import datetime,timedelta, timezone
from flask_restful import Resource
from flask import request
from pymongo.collection import Collection
from app.models import Item

from schema.SearchSchema import SearchParams

# from app import pymongo

from pymongo import MongoClient
client = MongoClient("mongodb://root:mongopw@localhost:27017/")
db = client["SearchDb"]

collection: Collection = db.items



class SearchResource(Resource):
    def get(self):
        

        try:
        # Parse and validate the incoming query parameters
            search_params = SearchParams(**request.args.to_dict())
        except Exception as e:
            return {"error": str(e)}, 400

        query = {}
        
        
        # Text search
        if search_params.searchTerm:
            query['$text'] = {'$search': search_params.searchTerm}

        # Filter by finished, ending soon, or ongoing auctions
        if search_params.filterBy == 'finished':
            query['auctionEnd'] = {'$lt': datetime.now(timezone.utc)}
        elif search_params.filterBy == 'endingSoon':
            query['auctionEnd'] = {'$lt': datetime.now(timezone.utc) + timedelta(hours=6), '$gt': datetime.now(timezone.utc)}
        else:
            query['auctionEnd'] = {'$gt' : datetime.now(timezone.utc)}

        # Filter by seller and winner
        if search_params.seller:
            query['seller'] = search_params.seller
        if search_params.winner:
            query['winner'] = search_params.winner

        # Pagination
        skip = (search_params.pageNumber - 1) * search_params.pageSize
        
       
        items = list(collection.find(query).skip(skip).limit(search_params.pageSize))
        
      

        total_count = collection.count_documents(query)
        page_count = (total_count + search_params.pageSize - 1) // search_params.pageSize
        
        return {
            "results": [Item(**doc).model_dump(mode='json') for doc in items],
            "pageCount": page_count,
            "totalCount": total_count
        }, 200
