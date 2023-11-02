from django.shortcuts import render
from .models import Olist
# Create your views here.
def html2(request):
    data=Olist.objects.all()
    pro={
        'd':data
    }
    return render(request,'home1.html',context=pro)