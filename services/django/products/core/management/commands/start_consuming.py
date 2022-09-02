import time

from django.core.management.base import BaseCommand
from core.broker import Broker


class Command(BaseCommand):
    """Django Command to start consuming broker messages"""

    def handle(self, *args, **options):
        self.stdout.write("About to connect to the broker messages exchange")
        message_broker = Broker()
        message_broker.consume()
        self.stdout.write("Started consuming")
