import pika
from config import get_settings

params = pika.URLParameters(get_settings().rabbit_url)
connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(exchange, body):
    channel.basic_publish(
        exchange="",
        routing_key="transactions",
        body=body,
        properties=pika.BasicProperties(
            delivery_mode=2,  # make message persistent
        ),
    )
    print(" [x] Sent %r" % body)
