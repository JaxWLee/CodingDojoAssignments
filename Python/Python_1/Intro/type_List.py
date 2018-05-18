def typeList(var):
    x = len(var)
    sum = 0
    y = ''
    for count in range (0,x):
        if isinstance(var[count],str)==True:
            y = y + ' ' + var[count]
        elif isinstance(var[count],float)==True or isinstance(var[count],int) == True:
            sum = sum + var[count]
    if y == '':
        print "The list you entered is of integer type"
        print "Sum:", sum
    elif sum == 0:
        print "The list you entered is of string type"
        print "String:", y
    else:
        print "The list you entered is of mixed type"
        print "Sum:", sum
        print "String:", y
l = ['magical unicorns',19,'hello',98.98,'world']
typeList(l)
l = ['magical','unicorns']
typeList(l)
l = [2,3,1,7,4,12]
typeList(l)
