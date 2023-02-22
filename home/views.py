<<<<<<< HEAD
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("This is home page")

def about(request):
    return HttpResponse("This is about page")

def services(request):
    return HttpResponse("This is services page")

def contact(request):
=======
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("This is home page")

def about(request):
    return HttpResponse("This is about page")

def services(request):
    return HttpResponse("This is services page")

def contact(request):
>>>>>>> 0e18a9c9404795ecc7fb50606ba899712d6bae4b
    return HttpResponse("This is contact page")