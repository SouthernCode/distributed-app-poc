import pika, json, os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "products.settings")
django.setup()

from core.broker import Broker

message_broker = Broker()

message_broker.consume()
