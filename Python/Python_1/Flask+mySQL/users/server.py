from flask import Flask,redirect,render_template,request,flash,session,url_for
from mysqlconnection import MySQLConnector
import re
import md5
import os, binascii # include this at the top of your file
salt = binascii.b2a_hex(os.urandom(15))
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
name_REGEX = re.compile('[a-zA-Z]')
app = Flask(__name__)
app.secret_key="THIS IS SECRET"
mysql = MySQLConnector(app,'users')
@app.route('/')
def first():
    return redirect('/users')
@app.route('/users')
def index():
    query="SELECT * FROM users"
    dbquery = mysql.query_db(query)
    length = len(dbquery)
    return render_template('index.html',dbquery = dbquery,length = length)
@app.route('/users/new')
def new_users():
    return render_template('new.html')
@app.route('/users/<id>/edit')
def edit_user(id):
    session['update'] = id
    query = "SELECT * FROM users WHERE id = :id"
    data={
        "id": id
    }
    dbquery = mysql.query_db(query,data)
    ident = int(dbquery[0]['id'])
    first_name = str(dbquery[0]['first_name'])
    last_name = str(dbquery[0]['last_name'])
    email = str(dbquery[0]['email'])
    return render_template('edit.html',ident = ident,first_name=first_name,last_name=last_name,email=email)
@app.route('/users/<id>')
def show_user(id):
    query = "SELECT * FROM users WHERE id = :id"
    data={
        "id":id
    }
    dbquery = mysql.query_db(query,data)
    return render_template('user.html', dbquery = dbquery)
@app.route('/users/create',methods=["POST"])
def create_user():
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
    if valid == False:
        flash('Registration Unsuccessful')
        return redirect('/users/new')
    else:
        query = "INSERT INTO users (first_name,last_name,email,created_at,updated_at) VALUES (:first_name,:last_name,:email,NOW(),NOW())"
        data = {
            "first_name":request.form["first_name"],
            "last_name":request.form["last_name"],
            "email":request.form["email"]
        }
        mysql.query_db(query,data)
        query = "SELECT id FROM users ORDER BY id DESC LIMIT 1"
        ident = mysql.query_db(query)
        print ident[0]['id']
    return redirect(url_for('show_user',id = int(ident[0]['id'])))

@app.route('/users/update', methods=["POST"])
def update_user():

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
    if valid == False:
        flash('Registration Unsuccessful')
        return redirect('')
    query = "UPDATE users SET first_name =:first_name, last_name=:last_name, email=:email, updated_at=NOW() WHERE id = :id"
    data = {
        "first_name":str(request.form('first_name')),
        "last_name":str(request.form('last_name')),
        "email":str(request.form('email')),
        "id": session['update']
    }
    mysql.query_db(query,data)
    return redirect(url_for('show_user',id = session['update']))

@app.route('/users/<id>/destroy')
def destroy_user(id):
    query="DELETE FROM users WHERE id = :id"
    data = {
        "id":id
    } 
    mysql.query_db(query,data)
    return redirect('/users')

app.run(debug=True)