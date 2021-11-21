from django.db.models import base
from django.urls import path
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from django.urls import path, include

from apsis.views import ClientViewSet, MailDropViewSet, RecipientViewSet
from rest_framework_nested.routers import NestedSimpleRouter

router = DefaultRouter()
router.register(r'clients', ClientViewSet, basename='client')

client_router = NestedSimpleRouter(router, r'clients', lookup="client")
client_router.register(r'maildrops', MailDropViewSet, basename='maildrop')

maildrops_router = NestedSimpleRouter(
    client_router, r'maildrops', lookup="maildrop")
maildrops_router.register(
    r'recipients', RecipientViewSet, basename='recipient')

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include(client_router.urls)),
    path(r'', include(maildrops_router.urls)),
]
