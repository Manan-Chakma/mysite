from django.urls import path
from rest_framework import routers
from .views import *


urlpatterns = [
    # /snippetlist/
    path('', ListSnippets.as_view()),
]
