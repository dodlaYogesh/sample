from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('Welcome to my Home')

def college(request):
    return HttpResponse('Welcome to my College')

def html(request):
    return render(request,'home.html')