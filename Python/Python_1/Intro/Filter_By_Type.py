def filterType(var):
    if isinstance(var,int)==True:
        if var >=100:
            print "That's a big number"
        else:
            print "That's a small number"
    elif isinstance(var,str)==True:
        if len(var)>=50:
            print "Long Sentence"
        else:
            print "Short Sentence"
    elif isinstance(var,list)==True:
        if len(var)>=10:
            print "Big List"
        else:
            print "Small List"
    else:
        print "Somethings Wrong"

sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']

filterType(sI)
filterType(mI)
filterType(bI)
filterType(eI)
filterType(spI)
filterType(sS)
filterType(mS)
filterType(bS)
filterType(eS)
filterType(aL)
filterType(mL)
filterType(lL)
filterType(eL)
filterType(spL)