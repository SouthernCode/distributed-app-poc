import time
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
        self.connection = self.__connect()
        self.channel = self.connection.channel()

    def __connect(self):
        """
        Connect to the broker
        Waits upto 3 minutes for the broker to be ready
        """
        timeout = time.time() + 60 * 3  # 3 minutes from now
        final_exceptions = None
        while time.time() < timeout:
            try:
                return pika.BlockingConnection(self.connection_params)
            except Exception as e:
                print(f"RabbitMQ is not ready yet... Waiting 1 second")
                time.sleep(1)
                final_exceptions = e
        raise Exception(
            f"RabbitMQ is not ready after 180 seconds... Exiting: {final_exceptions}"
        )

    def __close(self):
        """
        Close the connection to the broker
        """
        self.connection.close()

    def publish(self, body: dict, exchange: str = ""):
        """
        Publish a message to the broker
        """
        if self.connection.is_closed:
            self.connection = self.__connect()
            self.channel = self.connection.channel()
        self.channel.basic_publish(
            exchange="",
            routing_key="products",
            body=body,
            properties=pika.BasicProperties(
                delivery_mode=2,  # make message persistent
            ),
        )
        print(" [x] Sent %r" % body)
        self.__close()

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
        # self.channel.close()

    def consumer_callback(self, ch, method, properties, body):
        """
        Callback for consuming messages from the broker
        For now, just print the message body
        """
        print(f"Received message in transactions: {body}")
        pass
