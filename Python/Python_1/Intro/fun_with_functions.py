def odd_even(x,y):
    for count in range(x,y):
        if count%2 == 0:
            print "Number is "+ str(count) +". This is an even number."
        elif count%2 == 1:
            print "Number is "+ str(count)+". This is an odd number."

odd_even(1,2001)

def multiply(arr,num):
    x = len(arr)
    for count in range(0,x):
        arr[count] *= num
    return arr
a = [2,4,10,16]
b = multiply(a,5)
print b

def layered_multiply(arr):
    x = len(arr)
    for count in range(0,x):
        z =[]
        y = arr[count]
        for i in range (0,y):
            z.append(1)
        arr[count] = z
    print arr
layered_multiply([1,2,3])
a = [1,3,5]
layered_multiply(multiply(a,3))
