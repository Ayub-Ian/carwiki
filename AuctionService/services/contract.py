from flask import Flask, request, jsonify
from kombu import Connection, Exchange, Queue
import json

app = Flask(__name__)

# RabbitMQ connection
rabbitmq_url = 'amqp://guest:guest@localhost:5672/'
conn = Connection(rabbitmq_url)

# Define exchange and queue
exchange = Exchange('AuctionSvc.AuctionCreated', type='fanout')
queue = Queue('auction_created', exchange=exchange, routing_key=None)

@app.route('/api/endpoint', methods=['POST'])
def api_endpoint():
    data = request.json
    
    # Process the data
    result = process_data(data)
    
    # Publish the result to RabbitMQ
    with conn.Producer() as producer:
        producer.publish(
            json.dumps(result),
            exchange=exchange,
            routing_key='microservice_key',
            declare=[queue]
        )
    
    return jsonify({"status": "success"}), 200

def process_data(data):
    # Implement your data processing logic here
    return {"processed_data": data}


class ExchangeManager:
    def __init__(self, rabbitmq_url):
        self.connection = Connection(rabbitmq_url)
        self.exchanges = {}

    def declare_exchange(self, name, type='direct', durable=True):
        if name not in self.exchanges:
            exchange = Exchange(name, type=type, durable=durable)
            self.exchanges[name] = exchange
            with self.connection.channel() as channel:
                exchange.declare(channel=channel)
        return self.exchanges[name]

    def get_exchange(self, name):
        return self.exchanges.get(name)

    def list_exchanges(self):
        return list(self.exchanges.keys())

# Usage
rabbitmq_url = 'amqp://guest:guest@localhost:5672//'
manager = ExchangeManager(rabbitmq_url)

# Declare exchanges
user_exchange = manager.declare_exchange('user.created.v1')
order_exchange = manager.declare_exchange('order.updated.v1')

# Get all exchanges
all_exchanges = manager.list_exchanges()
print(f"All exchanges: {all_exchanges}")    