from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Question, Choice

def index(request):
    return HttpResponse("Hello World")

def details(self, question_id):
    return HttpResponse("Hello World")

def results(self, question_id):
    return HttpResponse("Hello World")

def votes(self, question_id):
    return HttpResponse("Hello World")