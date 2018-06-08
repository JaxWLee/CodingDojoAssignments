from flask import Flask,redirect,render_template,request,flash,session
from mysqlconnection import MySQLConnector
import re
import md5
import os, binascii # include this at the top of your file
salt = binascii.b2a_hex(os.urandom(15))
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
name_REGEX = re.compile('[a-zA-Z]')
app = Flask(__name__)
app.secret_key="THIS IS SECRET"
mysql = MySQLConnector(app,'login_registration')
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/register',methods=["POST"])
def register():
    valid=True
    if len(request.form['first_name'])<1:
        valid=False
        flash("First Name cannot be blank")
    if not name_REGEX.match(request.form['first_name']):
        valid=False
        flash("First Name can only consist of letters")
    if len(request.form['last_name'])<1:
        valid=False
        flash("Last Name cannot be blank")
    if not name_REGEX.match(request.form['last_name']):
        valid=False
        flash("Last Name can only consist of letters")
    if len(request.form['email'])<1:
        valid=False
        flash("Email cannot be blank")
    if not EMAIL_REGEX.match(request.form['email']):
        valid = False
        flash("Invalid Email Address!")
    if len(request.form['password'])<1:
        valid=False
        flash("Password cannot be blank")
    if len(request.form['password'])<8:
        valid=False
        flash("Password must be at least 8 characters long")
    if len(request.form['confirm_password'])<1:
        valid=False
        flash("Confirm Password cannot be blank")
    if request.form['password']!= request.form['confirm_password']:
        valid=False
        flash("Passwords much match")
    if valid == False:
        flash('Registration Unsuccessful')
        return redirect('/')
    else:
        query="INSERT INTO users (first_name,last_name,email,password,salt,created_at,updated_at) VALUES(:first_name,:last_name,:email,:password,:salt, NOW(),NOW())"
        data = {
            "first_name":request.form['first_name'],
            "last_name":request.form['last_name'],
            "email":request.form['email'],
            "password":md5.new(request.form['password'] + salt).hexdigest(),
            "salt":salt 
        }
        mysql.query_db(query,data)
        flash("Registration Successful")
        return redirect('/')
@app.route('/login',methods=["POST"])
def login():
    valid=True
    if len(request.form['email'])<1:
        valid=False
        flash("Email cannot be blank")
    if not EMAIL_REGEX.match(request.form['email']):
        valid = False
        flash("Invalid Email Address!")
    if len(request.form['password'])<1:
        valid=False
        flash("Password cannot be blank")
    if valid == True:
        query = "SELECT * FROM users WHERE email = :email"
        data = {
            "email":request.form['email']
        }
        dbquery = mysql.query_db(query,data)
        if len(dbquery) > 0:
            if md5.new(request.form['password'] + dbquery[0]['salt']).hexdigest() != dbquery[0]['password']:
                flash('Incorrect Password')
                return redirect('/')
            else:
                flash('Successful Log In')
                session['user'] = dbquery[0]['first_name'] + ' ' + dbquery[0]['last_name']
            return redirect('/dashboard')
        elif len(dbquery) == 0:
            flash('User Not Registered. Please Register Abover')
            return redirect('/')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
@app.route('/logout', methods=["POST"])
def logout():
    session.clear()
    return redirect('/')
    
app.run(debug=True)