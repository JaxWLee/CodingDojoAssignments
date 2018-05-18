from flask import Flask,render_template,redirect,request
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html', name = 'tmnt.png')
@app.route('/ninjas/<color>')
def page_view(color):
    if color =='blue':
        return render_template('ninjas.html',name = 'leonardo.jpg')
    elif color=='red':
        return render_template('ninjas.html',name = 'raphael.jpg')
    elif color=='orange':
        return render_template('ninjas.html',name = 'michelangelo.jpg')
    elif color=='purple':
        return render_template('ninjas.html',name = 'donatello.jpg')
    else:
        return render_template('ninjas.html',name = 'notapril.jpg')

app.run(debug=True)