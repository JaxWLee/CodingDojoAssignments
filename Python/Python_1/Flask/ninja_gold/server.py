from flask import Flask, session, redirect,render_template,request
app = Flask(__name__)
app.secret_key = 'ninjagold'
import random
import datetime




@app.route('/')
def index():
    if "total_gold" not in session:
        session["total_gold"] = 0
    if "activity" not in session:
        session["activity"] = []
    return render_template('index.html')
@app.route('/process_money',methods=["POST"])
def process_gold():
    building = request.form['building']
    if building == 'farm':
        gold = random.randint(10,20)
        session["total_gold"]+= gold
        session["activity"].append({
            "event":"Earned " + str(gold) + " gold from the farm " + str(datetime.datetime.now()),
            "won":True
        })
    elif building == 'cave':
        gold = random.randint(5,10)
        session["total_gold"]+= gold
        session["activity"].append(
            {"event":"Earned " + str(gold) + " gold from the cave " + str(datetime.datetime.now()),
            "won":True
            })

    elif building == 'house':
        gold = random.randint(2,5)
        session["total_gold"]+= gold
        session["activity"].append({
            "event":"Earned " + str(gold) + " gold from the house " + str(datetime.datetime.now()),
            "won":True
        })
    elif building == 'casino':
        chance = random.randint(1,2)
        gold = random.randint(0,50)
        if chance == 1:
            session["total_gold"]-= gold
            session["activity"].append({
                "event":"Entered a casino and lost " + str(gold) + " gold " + str(datetime.datetime.now()),
                "won":False
            })
        else:
            session["total_gold"]+= gold
            session["activity"].append({
                "event":"Entered a casino and won " + str(gold) + " gold " + str(datetime.datetime.now()),
                "won":True
            })
    return redirect('/')
@app.route('/clear')
def clear_session():
    session.clear()
    return redirect('/')
app.run(debug=True)