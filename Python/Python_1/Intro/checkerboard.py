def checkerboard():
    checkerboard1 = '*'
    checkerboard2 = ' '
    for count in range (0,7):
        if count%2==0:
            checkerboard1 = checkerboard1 + ' '
            checkerboard2 = checkerboard2 + '*'
        if count%2==1:
            checkerboard1 = checkerboard1 + '*'
            checkerboard2 = checkerboard2 + ' '
    for count in range (0,5):
        print checkerboard1
        print checkerboard2
checkerboard()