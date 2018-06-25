from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
import bcrypt
from models import *
# Create your views here.
def index(request):
    return render(request,'books/index.html')

def dashboard(request):
    context = {
        'recent':Review.objects.all().order_by('-created_at')[:3],
        'all': Book.objects.all()
    }

    return render(request,'books/dashboard.html',{"context": context})

def add(request):
    context = Author.objects.all()
    return render(request,'books/add.html',{'context':context})

def books(request,id):
    context = Book.objects.get(id = id)
    return render(request,'books/books.html',{"context":context})

def users(request,id):
    context = User.objects.get(id = id)
    reviews = len(User.objects.get(id = id).reviews.all())
    books = User.objects.get(id = id).reviews.all()
    return render(request,'books/users.html',{"context": context, 'reviews':reviews, 'books':books})

def process(request):
    if request.POST['form'] == 'register':
        error =  User.objects.validate(request.POST)
        if len(error) > 0:
            for i in error:
                messages.error(request,i)
            return redirect('/')
        else:
            hashpass = bcrypt.hashpw(request.POST['password'].encode(),bcrypt.gensalt())
            User.objects.create(name = request.POST['name'], user_name = request.POST['user_name'], email = request.POST['email'], password = hashpass)
        return redirect('/books/')

    elif request.POST['form'] == 'add':
        error = Book.objects.validate(request.POST)
        if len(error) > 0:
            for i in error:
                messages.error(request,i)
            return redirect('books/add/')
        else:
            if request.POST['add_author'] == '':
                Book.objects.create(title=request.POST['title'])
                Author.objects.get(id = request.POST['author']).books.append(Book.objects.last())
                Review.objects.create(content =request.POST['review'], book=Book.objects.last(),user= User.objects.get(id = request.session['id']))
            else:
                Author.objects.create(name = request.POST['add_author'])
                Book.objects.create(title=request.POST['title'], author = Author.objects.last())
                Review.objects.create(content =request.POST['review'], book=Book.objects.last(),user = User.objects.get(id = request.session['id']),rating = request.POST['rating'])
            
        return redirect('/books/')

    elif request.POST['form'] == 'login':
        error = User.objects.login(request.POST)
        if len(error) == 0:
            user = User.objects.filter(email = request.POST['email'])
            request.session['id'] = user[0].id
            request.session['name'] = user[0].name
            return redirect('/books/')
        else:
            return redirect('/')
    
    elif request.POST['form'] == "add_review":
        Review.objects.create(content = request.POST['review'],rating = request.POST['rating'], book = Book.objects.get(id = request.POST['book']), user = User.objects.get(id = request.session['id']) )

        return redirect('/books/{}'.format(request.POST['book']))


def logout(request):
    request.session.clear()
    return redirect('/')