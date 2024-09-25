from kombu import Connection, Exchange, Queue


# RabbitMQ connection
rabbitmq_url = 'amqp://guest:guest@localhost:5672/'

class ExchangeManager:
    def __init__(self):
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
    
    def publish(self, body: dict, exchange: str, queue):

        task_queue = Queue(queue, exchange=self.get_exchange(exchange))

        with self.connection.Producer() as producer:

            if not isinstance(body, dict):
                raise ValueError("Body must be a dictionary")
                
            producer.publish(
                body,
                exchange=self.get_exchange(exchange),
                declare=[task_queue]
            )

