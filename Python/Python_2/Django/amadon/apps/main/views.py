from django.shortcuts import render, redirect

def index(request):
    if 'total_spent' not in request.session:
        request.session['total_spent'] = 0
        request.session['total_items'] = 0
    return render(request,'main/index.html')

def process(request):
    if int(request.POST["product_id"]) == 1:
        request.session['charge'] = 19.99 * int(request.POST['quantity'])
        request.session['total_spent']+= request.session['charge']
        request.session['total_items']+= int(request.POST['quantity'])
    elif int(request.POST["product_id"]) == 2:
        request.session['charge'] = 29.99 * int(request.POST['quantity'])
        request.session['total_spent']+= request.session['charge']
        request.session['total_items']+= int(request.POST['quantity'])
    elif int(request.POST["product_id"]) == 3:
        request.session['charge'] = 4.99 * int(request.POST['quantity'])
        request.session['total_spent']+= request.session['charge']
        request.session['total_items']+= int(request.POST['quantity'])
    elif int(request.POST["product_id"]) == 4:
        request.session['charge'] = 49.99 * int(request.POST['quantity'])
        request.session['total_spent']+= request.session['charge']
        request.session['total_items']+= int(request.POST['quantity'])
    print request.POST['product_id']
    print request.session['total_spent']
    print request.session['total_items']
    return redirect('/store/checkout/')

def checkout(request):
    return render(request,'main/checkout.html')
# Create your views here.