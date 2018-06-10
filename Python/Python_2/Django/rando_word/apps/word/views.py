from django.shortcuts import render,redirect,HttpResponse
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    if 'number' not in request.session:
        request.session['number'] = 0
        request.session['word'] = ''
    else:
        request.session['number'] += 1
        request.session['word'] = get_random_string(length=14)
    context = {
        'number': request.session['number'],
        'word':  request.session['word']
    }
    return render(request,"word/index.html",context)

def generate(request):
    return redirect('/random_word')

def clear(request):
    request.session.clear()
    return redirect('/random_word')
