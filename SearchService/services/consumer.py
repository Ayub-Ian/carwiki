from kombu import Connection, Exchange, Queue
from kombu.mixins import ConsumerMixin
from pymongo import MongoClient, ASCENDING
from pymongo.errors import ConnectionFailure, BulkWriteError


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
            Queue("auction_deleted",Exchange("AuctionSvc.AuctionDeleted", type="fanout"))
        ]
        
    def get_consumers(self, Consumer, channel):
        return [
            Consumer(queues=self.queues[0],callbacks=[self.on_created]),
            Consumer(queues=self.queues[1],callbacks=[self.on_deleted]),
        ]
    
    def on_created(self, body, message):
        if db is not None:
            collection = db['items']

            if body:
                 
                 collection.insert_one(body)
                 message.ack()

    def on_deleted(self, body, message):
        if db is not None:
            collection = db['items']

            if body:
                
                item_id = body.get("id")
                
                if item_id:
                    result  = collection.delete_one({"id": item_id})
                    
                    if result.deleted_count > 0:
                        print("Item deleted")
                        message.ack()
                    else:
                        message.reject()
                else:
                    message.reject()


if __name__ == "__main__":

 
    with Connection(rabbitmq_url, heartbeat=4) as conn:
            worker = Worker(conn)
            worker.run()