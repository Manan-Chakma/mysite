from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
# Create your views here.


class ListSnippets(APIView):
    def get(self, request, format=None):
        return HttpResponse("Hello World")
