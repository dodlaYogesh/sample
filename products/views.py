from django.shortcuts import render
from django.http import HttpResponse
from .models import list

# Create your views here.

def home(request):
    return HttpResponse('Welcome to my Home')

def college(request):
    return HttpResponse('Welcome to my College')

def html(request):
    data=list.objects.all()

    pro={
        'd':data
    }
    return render(request,'home.html',context=pro)