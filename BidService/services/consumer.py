from kombu import Connection, Exchange, Queue
from kombu.mixins import ConsumerMixin
from pymongo import MongoClient, ASCENDING
from pymongo.errors import ConnectionFailure, BulkWriteError
from app.models import Auction

rabbitmq_url = 'amqp://guest:guest@localhost:5672/'
MONGO_URI = "mongodb://root:mongopw@localhost:27017/"
DB_NAME = "SearchDb"

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


db = connect_to_mongo(MONGO_URI, DB_NAME)



class Worker(ConsumerMixin):
    def __init__(self, connection):
        self.connection = connection
        self.queues = [
            Queue("auction_created",Exchange("AuctionSvc.AuctionCreated", type="fanout")),
        ]
        
    def get_consumers(self, Consumer, channel):
        return [
            Consumer(queues=self.queues,callbacks=[self.on_created]),
        ]
    
    def on_created(self, body, message):
        if db is not None:
            collection = db['auctions']

            if body:
                
                auction = Auction(**body)
                 
                collection.insert_one(auction.model_dump_json())
                message.ack()

if __name__ == "__main__":

 
    with Connection(rabbitmq_url, heartbeat=4) as conn:
            worker = Worker(conn)
            worker.run()