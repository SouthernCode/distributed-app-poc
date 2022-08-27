import pika

RABBIT_URL = ""

params = pika.URLParameters(RABBIT_URL)
connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue="transaction")


def callback(ch, method, properties, body):
    print(f"Received message in transactions: {body}")
    pass


channel.basic_consume(queue="transaction", on_message_callback=callback)

print("Started consuming")

channel.start_consuming()

channel.close()
