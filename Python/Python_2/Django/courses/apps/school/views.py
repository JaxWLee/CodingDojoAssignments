from django.shortcuts import render,redirect
from models import *
from django.contrib import messages

def index(request):
    context = Course.objects.all()
    return render(request,'school/index.html',{'context':context})

def add(request):
    error = Course.objects.valid(request.POST)
    if len(error) == 0:
        Course.objects.create(name = request.POST['name'], desc = Description.objects.create(content = request.POST['description']))
    else:
        for i in error:
            messages.error(request,i)
    return redirect('/')

def comments(request,id):
    context = Course.objects.get(id = id)
    comments = Course.objects.get(id = id).comments.all()
    return render(request,'school/comments.html',{'context': context, 'comments':comments})

def add_comment(request,id):
    Course.objects.get(id = id).comments.create(content = request.POST['new_comment'])
    return redirect('/{}/comments'.format(id))

def destroy(request,id):
    context = Course.objects.get(id = id)
    return render(request,'school/destroy.html',{'context':context})

def process(request,id):
    Course.objects.get(id=id).delete()
    return redirect('/')
    
    # Create your views here.
