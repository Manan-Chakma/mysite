from django.core.management.base import BaseCommand
from faker import Faker
import faker

from apsis.models import Client, MailDrop, MailRecipent

class ClientCreateCommand(BaseCommand):
    help = "command information"

    def handle(self, *args, **options):
        fake = Faker()
        clients = []
        for _ in range(10):
            clients.append(Client(name= fake.name()))
        
        Client.objects.bulk_create(clients)

