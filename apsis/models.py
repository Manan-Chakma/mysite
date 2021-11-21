from django.db import models

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=255)


class MailDrop(models.Model):
    title = models.CharField(max_length=255)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)



class MailRecipent(models.Model):
    name = models.CharField(max_length=255)
    mail_drop_id = models.ForeignKey(MailDrop, on_delete= models.CASCADE)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)