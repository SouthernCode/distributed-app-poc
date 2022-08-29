import pika

from config import get_settings

# RABBIT_URL = "amqp://{RABBITMQ_DEFAULT_USER}:{RABBITMQ_DEFAULT_PASS}@{RABBITMQ_HOST}"

params = pika.URLParameters(get_settings().rabbit_url)
connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue="transactions")


def callback(ch, method, properties, body):
    print(f"Received message in transactions: {body}")
    pass


channel.basic_consume(queue="transactions", on_message_callback=callback)

print("Started consuming")

channel.start_consuming()

channel.close()
