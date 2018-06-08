from django.shortcuts import render,HttpResponse,render,redirect
from django.contrib import messages
from time import gmtime,strftime
from django.utils.crypto import get_random_string

def index(request):
    context = {
        "date": strftime("%Y-%m-%d",gmtime()),
        "time": strftime("%H:%M %p",gmtime())
    }
    return render(request,'disp_time/index.html',context)
# Create your views here.
