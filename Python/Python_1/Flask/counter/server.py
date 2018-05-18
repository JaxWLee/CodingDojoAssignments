from flask import Flask,render_template,redirect,request,session
import os
app = Flask(__name__)
app.secret_key = os.urandom(24)
counter = 1
@app.route('/')
def index():
    session['counter'] = counter
    return render_template('index.html')
@app.route('/counter',methods=["POST"])
def countered():
    if request.form['name'] == "start":
        session['counter']+= 1
        return render_template('index.html')
    elif request.form['name'] == "twos":
        session['counter']+= 2
        return render_template('index.html')
    elif request.form['name'] == "reset":
        return redirect('/')
app.run(debug=True)