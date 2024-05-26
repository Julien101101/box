from django.http import Http404
from .models import Shape
from django.shortcuts import render


def home(request):
    return render(request, "shapes/index.html")

def profile(request):
    return render(request, "profile.html")


def shaooo(request):
    return render(request, "contact.html")
