from flask import Flask,render_template,redirect,request,flash,session
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/results',methods=['POST'])
def result():
    if len(request.form['name']) < 1 or len(request.form['comment']) > 120 or len(request.form['comment']) < 1:
        if len(request.form['name']) < 1 and len(request.form['comment']) < 120 and len(request.form['comment']) > 1:
            flash('Name Cannot Be Blank')
        elif len(request.form['name']) >= 1 and len(request.form['comment']) > 120:
            flash('Comment cannot be longer than 120 characters')
        elif len(request.form['name']) < 1 and len(request.form['comment']) > 120:
            flash('Name Cannot Be Blank')
            flash('Comment cannot be longer than 120 characters')
        elif len(request.form['name']) < 1 and len(request.form['comment']) < 1:
            flash('Name Cannot Be Blank')
            flash('Comment Cannot Be Blank')
        elif len(request.form['name']) > 1 and len(request.form['comment']) < 1:
            flash('Comment Cannot Be Blank')
        return redirect('/')
    else:
        flash("Success")
    return render_template('results.html',name = request.form['name'], dojo = request.form['dojo'], favorite = request.form['favorite_language'], comment = request.form['comment'])

app.run(debug=True)