from django.core.management.base import BaseCommand
from faker import Faker

from apsis.models import Client, MailDrop, MailRecipent

class CreateMailDropFakeDataCommand(BaseCommand):
    help = "command information"

    def handle(self, *args, **options):
        fake = Faker()
        client_obj = Client.objects.filter()

        mail_drop = []
        for i in range(10):
            for _ in range(2):
                mail_drop.append(MailDrop(title= fake.name(), client_id= client_obj[i]))
        

        MailDrop.objects.bulk_create(mail_drop)

