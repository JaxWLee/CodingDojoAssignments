from flask import Flask,render_template,redirect,request,flash,session
import re
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/process', methods = ['POST'])
def process():
    PASSWORD_REGEX = re.search(r'^\d.*[A-Z]|[A-Z].*\d',request.form['password'])
    if request.form['email'] < 1 or request.form['first_name'] < 1 or request.form['last_name'] < 1 or request.form['password'] < 1 or request.form['confirm_password'] < 1:
        if request.form['email'] < 1:
            flash('Email cannot be blank')  
        elif request.form['first_name'] < 1:
            flash('First Name cannot be blank')
        elif request.form['last_name'] < 1:
            flash('Last_name cannot be blank')
        elif request.form['password'] < 1:
            flash('Password cannot be blank')
        elif request.form['confirm_password'] < 1:
            flash('Confirm Password cannot be blank')
    elif request.form['password'] != request.form['confirm_password']:
        flash('Passwords must match')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
    elif PASSWORD_REGEX == None:
        flash("Password must have at least one uppercase letter and one number")
    else:
        flash('Thanks for submitting your information.')
    
    return redirect('/')
app.run(debug=True)