from flask import Flask,render_template,redirect
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html',name ="dojo")
@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html')
@app.route('/dojo/new')
def dojonews():
    return render_template('dojos.html')
@app.route('/dojo/new',methods=['POST'])
def submit():
    return redirect('/dojo/new')
app.run(debug=True) 