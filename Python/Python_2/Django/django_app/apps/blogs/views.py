from django.shortcuts import render,HttpResponse, redirect

def index(request):
    response="placeholder to later display all the list of blogs"
    return HttpResponse(response)
def new(request):
    response="placeholder to display a new form to create a new blog"
    return HttpResponse(response)
def show(request,number):
    response = "place holder to display blog number " + number
    return HttpResponse(response)
def create(request):
    return redirect('/') 
def edit(request,number):
    response = "place order to edit blog " + number
    return HttpResponse(response)
def destroy(request):
    return redirect("/")
# Create your views here.