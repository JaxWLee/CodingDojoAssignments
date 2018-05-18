from flask import Flask,request,redirect,session,render_template
import random # import the random module
# The random module has many useful functions. This is one that gives a random number in a range

app = Flask(__name__)
app.secret_key = 'somekey'
@app.route('/')
def index():
    session['random'] = random.randrange(0,101)
    return render_template('index.html')
@app.route('/other',methods=["POST"])
def other():
    r = request.form['text']
    q = int(r)
    if q == session['random']:
        #adding = r + """ was the number!""" + '''<form action='/'> <input type="submit" value = "Play Again"></form>'''
        return render_template('win.html',r = r)
    elif q < session['random']:
        adding = """Too Low"""
        return render_template('other.html',adding = adding,r = r)
    elif q > session['random']:
        adding = """Too High"""
        return render_template('other.html',adding = adding,r = r)
app.run(debug=True)
