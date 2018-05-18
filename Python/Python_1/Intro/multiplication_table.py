x = [1,2,3,4,5,6,7,8,9,10,11,12]
print 'x', x
for count in range(1,13):
    y = count
    for count in range(0,12):
        x[count] = y * x[count]
    print (*("{:3}".format(row*col) for col in range(1, n+1)))
    x = [1,2,3,4,5,6,7,8,9,10,11,12]
