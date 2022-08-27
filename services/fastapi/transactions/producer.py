import pika

RABBIT_URL = ""

params = pika.URLParameters(RABBIT_URL)
connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(exchange, body):
    channel.basic_publish(
        exchange="",
        routing_key="transaction",
        body=body,
        properties=pika.BasicProperties(
            delivery_mode=2,  # make message persistent
        ),
    )
    print(" [x] Sent %r" % body)
