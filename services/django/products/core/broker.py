import time
import pika
import json

from django.conf import settings

from core.events.new_transaction_event_handler import handle_new_transaction
from core.events.schemas.transaction_schemas import TransactionSchema

ROUTING_KEY = "products"  # Maybe this should be a configurable parameter


class Broker:
    """
    Class in charge of connecting to the RabbitMQ broker
    Handles publishing and consuming messages
    """

    def __init__(self):
        self.connection_params = pika.URLParameters(settings.RABBITMQ_URL)
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

    def publish(self, exchange, body):
        """
        Publish a message to the broker
        """
        if self.connection.is_closed:
            self.connection = self.__connect()
            self.channel = self.connection.channel()
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
        # self.channel.exchange_declare(exchange="", exchange_type="direct")
        # self.channel.queue_declare(queue=ROUTING_KEY)
        self.channel.basic_consume(
            queue=ROUTING_KEY, on_message_callback=self.consumer_callback
        )
        print("Started consuming")
        self.channel.start_consuming()
        # self.channel.close()

    def consumer_callback(self, ch, method, properties, body: str):
        """
        Callback for consuming messages from the broker
        For now, just print the message body
        """
        print(f"Received message in transactions: {body}")
        print(f"method: {method}")
        parsed_body = json.loads(body)
        print(f"Parsed body: {parsed_body}")
        print(f'Action: {parsed_body.get("action")}')
        action = parsed_body.get("action")
        if action == "created":
            print("A transaction has been created")
            new_transaction = TransactionSchema(**parsed_body.get("transaction"))
            handle_new_transaction(new_transaction)
            ch.basic_ack(delivery_tag=method.delivery_tag)  # acknowledge the message
        pass
