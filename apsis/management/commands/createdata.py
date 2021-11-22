from django.core.management.base import BaseCommand
from faker import Faker

from apsis.models import Client, MailDrop, MailRecipent

class Command(BaseCommand):
    help = "client create dummy data command"

    def handle(self, *args, **options):
        fake = Faker()
        clients = []
        for _ in range(10):
            clients.append(Client(name= fake.name()))
        
        Client.objects.bulk_create(clients)

