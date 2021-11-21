from http import client
import re
from django.db.models import query
from django.shortcuts import get_object_or_404, render

from apsis.serializers import ClientSerializer, MailDropSerializer, MailRecipientSerializer
from .models import *
from rest_framework import viewsets
from rest_framework.response import Response


class ClientViewSet(viewsets.ViewSet):
    serializer_class = ClientSerializer

    def list(self, request):
        queryset = Client.objects.filter()
        serializer = ClientSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Client.objects.filter()
        client = get_object_or_404(queryset, pk=pk)
        serializer = ClientSerializer(client)
        return Response(serializer.data)

    def create(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass


class MailDropViewSet(viewsets.ViewSet):
    serializer_class = MailDropSerializer

    def list(self, request, client_pk=None):
        queryset = MailDrop.objects.filter(client_id=client_pk)
        serializer = MailDropSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, client_pk=None):
        queryset = MailDrop.objects.filter(pk=pk, client_id=client_pk)
        maildrop = get_object_or_404(queryset, pk=pk)
        serializer = MailDropSerializer(maildrop)
        return Response(serializer.data)


class RecipientViewSet(viewsets.ViewSet):
    serializer_class = MailRecipientSerializer

    def list(self, request, client_pk=None, maildrop_pk=None):
        queryset = MailRecipent.objects.filter(
            client_id=client_pk, mail_drop_id=maildrop_pk)
        serializer = MailRecipientSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, client_pk=None, maildrop_pk=None):
        queryset = MailRecipent.objects.filter(
            client_id=client_pk, mail_drop_id=maildrop_pk)
        mailrecipent = get_object_or_404(queryset, pk=pk)
        serializer = MailRecipientSerializer(mailrecipent)
        return Response(serializer.data)
