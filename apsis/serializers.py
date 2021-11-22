from django.db.models import fields
from rest_framework_nested.relations import NestedHyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework_nested.serializers import NestedHyperlinkedModelSerializer
from rest_framework.serializers import IntegerField

from .models import *

class ClientSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name']


class MailDropSerializer(NestedHyperlinkedModelSerializer):
    parent_lookup_kwargs = {
        'client_pk': 'client_id',
    }

    client_id = IntegerField(source='client_id.id')


    class Meta:
        model = MailDrop
        fields = ['id', 'title', 'client_id']


class MailRecipientSerializer(NestedHyperlinkedModelSerializer):
    parent_lookup_kwargs = {
        'maildrop_pk': 'mail_drop_id',
        'client_pk': 'client_id'
    }

    class Meta:
        model = MailRecipent
        fields = ['id', 'name']
