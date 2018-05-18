def scores_grades(num):
    print "Scores and Grades:"
    import random
    for i in range(0,num):
        x = random.random()*40+60
        x = round(x,0)
        if x < 70:
            print "Score: "+str(x)+"; Your grade is D"
        elif x < 80:
            print "Score: "+str(x)+"; Your grade is C"
        elif x < 90:
            print "Score: "+str(x)+"; Your grade is B"
        elif x <= 100:
            print "Score: "+str(x)+"; Your grade is A"
        
scores_grades(10)