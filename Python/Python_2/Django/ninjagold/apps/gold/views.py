from django.shortcuts import render,redirect
import random
from time import strftime
activities = []
def index(request):
    if 'total_gold' not in request.session:
        request.session['total_gold'] = 0
    return render(request,'gold/index.html')

def process(request):
    if request.POST['place'] == 'farm':
        gold = random.randint(10,20)
        activities.append({ 
            "event":'You earned ' + str(gold) + ' gold from the farm ' + strftime('%c'),
            'won': True
        })
        request.session['activities'] = activities
        request.session['total_gold'] += gold
        
    if request.POST['place'] == 'cave':
        gold = random.randint(5,10)
        activities.append({
            'event':'You earned ' + str(gold) + ' gold from the cave ' + strftime('%c'),
            'won': True
        })
        request.session['activities'] = activities
        request.session['total_gold'] += gold
        
    if request.POST['place'] == 'house':
        gold = random.randint(2,5)
        activities.append({
            "event":'You earned ' + str(gold) + ' gold from the house ' + strftime('%c'),
            'won': True
        })
        request.session['activities'] = activities
        request.session['total_gold'] += gold
        
    if request.POST['place'] == 'casino':
        chance = random.randint(0,1)
        if chance == 1:
            gold = random.randint(0,50)
            activities.append({
                "event":'You earned ' + str(gold) + ' gold from the casino ' + strftime('%c'),
                'won': True
            })
            request.session['activities'] = activities
            request.session['total_gold'] += gold
            
        else:
            gold = random.randint(0,50)
            activities.append({
                "event":'You lost ' + str(gold) + ' gold from the casino ' + strftime('%c'),
                'won': False
            })
            request.session['activities'] = activities
            request.session['total_gold'] -= gold
            
    return redirect('/')
def clear(request):
    request.session.clear()
    activities = []
    return redirect('/')
# Create your views here.
