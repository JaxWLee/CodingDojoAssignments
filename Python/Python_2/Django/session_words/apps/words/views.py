from django.shortcuts import render,redirect,HttpResponse
from time import strftime

savedlist = []
def index(request):
    return render(request,'words/index.html')

def process(request):
    if 'font' not in request.POST:
        context ={
            'word': request.POST['word'],
            'color':request.POST['color'],
            'time':strftime('%m/%d/%Y %H:%M')
        }
        print context['word']
        print context['color']
    else:
        context ={
            'word': request.POST['word'],
            'color':request.POST['color'],
            'font':request.POST['font'],
            'time':strftime('%m/%d/%Y %H:%M')
        }
    savedlist.append(context)
    request.session['words'] = savedlist

    return redirect('/session_words',context)
def clear(request):
    savedlist = []
    request.session.clear()
    return redirect('/session_words')
# Create your views here.
