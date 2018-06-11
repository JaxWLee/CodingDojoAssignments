from django.shortcuts import render,redirect,HttpResponse

def index(request):
    if 'number' not in request.session:
        request.session['number'] = 0
    return render(request,'form/index.html')
def process(request):
    request.session['context'] = {
        'name': request.POST['name'],
        'location': request.POST['location'],
        'language': request.POST['language'],
        'comment': request.POST['comment']
    }
    request.session['number'] += 1
    print request.session['context']['name']
    print request.session['context']['location']
    print request.session['context']['language']
    print request.session['context']['comment']
    return redirect('/survey/result')
def result(request):
    return render(request,'form/result.html')
# Create your views here.
