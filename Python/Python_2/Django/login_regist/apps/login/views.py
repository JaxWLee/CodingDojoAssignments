from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from models import *
# Create your views here.
def index(request):
    return render(request,'login/index.html')

def register(request):
    error = User.objects.validate(request.POST)
    if len(error) == 0:
        User.objects.create(first_name = request.POST['first_name'],last_name = request.POST['last_name'], email = request.POST['email'], password = bcrypt.hashpw(request.POST['password'].encode(),bcrypt.gensalt()))
        request.session['action'] = 'registered'
        request.session['user'] = User.objects.get(email = request.POST['email']).id
        return redirect('/dashboard/')
    else:
        for i in error:
            messages.error(request,i)
        return redirect('/')

def login(request):
    try:
        user = User.objects.filter(email = request.POST['email'])
        value = bcrypt.checkpw(request.POST['password'].encode(),User.objects.filter(email = request.POST['email']).first().password.encode())
        if len(user) == 0:
            messages.error(request, 'Email does not exist. Please register to create an account.')
            return redirect('/')
        elif value == True:
            request.session['user'] = User.objects.get(email = request.POST['email']).id
            request.session['action'] = 'logged in'
            print request.session['user'],User.objects.get(id = request.session['user']).first_name
            return redirect('/dashboard/')
        else:
            messages.error(request, 'Incorrect Password')
            print hash, User.objects.filter(email = request.POST['email']).first().password
            return redirect('/')
    except:
        return redirect('/')
def dashboard(request):
    context = User.objects.get(id = request.session['user'])

    return render(request,'login/dashboard.html',{'context':context})
