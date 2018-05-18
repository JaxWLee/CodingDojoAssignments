for count in range (1,1000): #odd numbers from 1 to 1000
    if count%2 != 0:
        print count
for count in range (1,1000001): #multiples of 5 from 5 to 1,000,000
    if count%5 == 0:
        print count
a = [1, 2, 5, 10, 255, 3]
x = sum(a) #sum of each element in a
print x
y = x/len(a) #average of the elements in a
print y
