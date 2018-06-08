from flask import Flask,redirect,render_template,request,flash,session
from mysqlconnection import MySQLConnector
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key="THIS IS SECRET"
mysql = MySQLConnector(app,'emailsdb')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process',methods=["POST"])
def process():
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")
        return redirect('/')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
        return redirect('/')
    else:
        query = "INSERT INTO emails (email,created_at,updated_at) VALUES (:email,NOW(),NOW())"
        data ={ "email": request.form["email"] }
        flash("The email address you entered " + request.form["email"] + " is valid. Thank You!" )
        mysql.query_db(query, data)
        return redirect('/success')
@app.route('/success')
def success():
    query = "SELECT * FROM emails"
    all_emails=mysql.query_db(query)
    return render_template('success.html', all_emails = all_emails)
@app.route('/remove',methods=["POST"])
def remove():
    query = "DELETE FROM emails WHERE id = :id"
    data = {
        "id":request.form['remove_number']
        }
    mysql.query_db(query,data)
    return redirect('/success')


app.run(debug=True)