# from django.shortcuts import render
from django.http import HttpResponse


def home_view(request):
    return HttpResponse('home')

def places_view(request):
    return HttpResponse('places')