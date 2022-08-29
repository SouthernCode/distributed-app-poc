import pika

from config import get_settings

ROUTING_KEY = "transactions"  # Maybe this should be a configurable parameter


class Broker:
    """
    Class in charge of connecting to the RabbitMQ broker
    Handles publishing and consuming messages
    """

    def __init__(self):
        self.connection_params = pika.URLParameters(get_settings().rabbit_url)
        self.connection = pika.BlockingConnection(self.connection_params)
        self.channel = self.connection.channel()

    def publish(self, exchange, body):
        """
        Publish a message to the broker
        """
        self.channel.basic_publish(
            exchange="",
            routing_key=ROUTING_KEY,
            body=body,
            properties=pika.BasicProperties(
                delivery_mode=2,  # make message persistent
            ),
        )
        print(" [x] Sent %r" % body)

    def consume(self):
        """
        Consume messages from the broker
        """
        self.channel.exchange_declare(exchange=ROUTING_KEY, exchange_type="direct")
        self.channel.queue_declare(queue=ROUTING_KEY)
        self.channel.basic_consume(
            queue=ROUTING_KEY, on_message_callback=self.consumer_callback
        )
        print("Started consuming")
        self.channel.start_consuming()
        self.channel.close()

    def consumer_callback(self, ch, method, properties, body):
        """
        Callback for consuming messages from the broker
        For now, just print the message body
        """
        print(f"Received message in transactions: {body}")
        pass
