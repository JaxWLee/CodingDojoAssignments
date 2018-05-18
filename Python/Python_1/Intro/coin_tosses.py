def coin_tosses():
    import random
    heads = 0
    tails = 0
    for i in range(0,5000):
        x = random.random()
        x = round(x)
        if x == 1:
            heads += 1
            print "Attempt #"+str(i+1)+" Coin is tossed.... Its a heads.... Got "+str(heads)+" heads and "+str(tails)+" tails so far"
        if x == 0:
            tails += 1
            print "Attempt #"+str(i+1)+" Coin is tossed.... Its a tails.... Got "+str(heads)+" heads and "+str(tails)+" tails so far"
coin_tosses()
