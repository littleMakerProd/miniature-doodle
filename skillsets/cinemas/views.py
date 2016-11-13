from django.shortcuts import render
from cinemas.models import Movie
# Create your views here.
from django.http import HttpResponse
from django.core import serializers
from django.http import JsonResponse

def index(request):
    return HttpResponse("You are at INDEX.") 

def get_movies_today(request):
    return HttpResponse(serializers.serialize('json',Movie.objects.all()), content_type="application/json")
