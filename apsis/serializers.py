from django.db.models import fields
from rest_framework_nested.relations import NestedHyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework_nested.serializers import NestedHyperlinkedModelSerializer
from .models import *

class ClientSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ['name']


class MailDropSerializer(NestedHyperlinkedModelSerializer):
    parent_lookup_kwargs = {
        'client_pk': 'client_id',
    }

    class Meta:
        model = MailDrop
        fields = ['title']


class MailRecipientSerializer(NestedHyperlinkedModelSerializer):
    parent_lookup_kwargs = {
        'maildrop_pk': 'mail_drop_id',
        'client_pk': 'client_id'
    }

    class Meta:
        model = MailRecipent
        fields = ['name', 'client_id', 'mail_drop_id']
