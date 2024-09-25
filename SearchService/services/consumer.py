from kombu import Connection, Exchange, Queue
from kombu.mixins import ConsumerMixin
rabbitmq_url = 'amqp://guest:guest@localhost:5672/'

class Worker(ConsumerMixin):
    def __init__(self, connection):
        self.connection = connection
        self.queues = [Queue("auction_created",Exchange("AuctionSvc.AuctionCreated", type="fanout"))]
    def get_consumers(self, Consumer, channel):
        return [Consumer(queues=self.queues,
                         callbacks=[self.on_message])]
    def on_message(self, body, message):
        print('Got message: {0}'.format(body))
        message.ack()



if __name__ == "__main__":

 
    with Connection(rabbitmq_url, heartbeat=4) as conn:
            worker = Worker(conn)
            worker.run()