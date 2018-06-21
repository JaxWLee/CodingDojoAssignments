from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from models import *

def index(request):
    context = User.objects.all()

    return render(request,'users/index.html',{'context':context})

def new(request):
    return render(request,'users/new.html')

def create(request):
    post_Data = request.POST
    error = User.objects.valid(post_Data)
    if len(error) == 0:
        User.objects.create(first_name = request.POST['first_name'],last_name = request.POST['last_name'], email = request.POST['email'])
        return redirect('/users')
    else:
        for i in error:
            messages.error(request,i)

        return redirect('/users/new')

def edit(request,id):
    request.session['id'] = id
    context = User.objects.get(id = id)
    return render(request,'users/update.html',{'context':context})

def show(request,id):
    context = User.objects.get(id = id)
    return render(request,'users/show.html',{'context':context})

def destroy(request,id):
    User.objects.get(id = id).delete()
    return redirect('/users/')

def update(request):
    user = User.objects.get(id = request.session['id'])
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.email = request.POST['email']
    user.save()
    return redirect('/users/')
