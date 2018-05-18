from flask import Flask,render_template,redirect,request
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/')
def post():
    return redirect('/results')
@app.route('/results',methods=['POST'])
def result():
    return render_template('results.html',name = request.form['name'], dojo = request.form['dojo'], favorite = request.form['favorite_language'], comment = request.form['comment'])

app.run(debug=True)