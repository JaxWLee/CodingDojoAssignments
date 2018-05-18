from flask import Flask, render_template, redirect, session, request
from datetime import datetime
import os
import random
app = Flask(__name__)
app.secret_key = os.urandom(23)
@app.route('/')
def index():
    if 'gold' in session:
        session['gold'] = session['gold']
    else:
        session['gold'] = 0
        session['activity'] = ''
    return render_template('index.html')
@app.route('/process_money')
def process_money():
    if request.form['gold'] == 'farm':
        a = random.randrange(0,11)
        b = 10 + a
        session['gold'] += b
        session['activity'] = session['activity'] + """ <p> Earned """ + str(b) + """form the farm """ +str(datetime.now())+"""</p>"""
        return redirect('/')
    elif request.form['gold'] == 'cave':
        a = random.randrange(0,6)
        b = 5 + a
        session['gold'] += b
        session['activity'] = session['activity'] + """ <p> Earned """ + str(b) + """form the cave """ +str(datetime.now())+"""</p>"""
        return redirect('/')
    elif request.form['gold'] == 'house':
        a = random.randrange(0,4)
        b = 2 + a
        session['gold'] += b
        session['activity'] = session['activity'] + """ <p> Earned """ + str(b) + """form the house """ +str(datetime.now())+"""</p>"""
        return redirect('/')
    elif request.form['gold'] == 'casino':
        a = random.randrange(-50,51)
        session['gold'] += a
        activity = 'Earned' + str(a) + 'form the casino' +str(datetime.now())
        return redirect('/')

app.run(debug=True)