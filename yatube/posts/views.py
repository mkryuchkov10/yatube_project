from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('Its main page of our social network')


def group_posts(request, slug):
    return HttpResponse(f'In this page you can see posts grouped by <h1> "{slug}" </h1> theme.')