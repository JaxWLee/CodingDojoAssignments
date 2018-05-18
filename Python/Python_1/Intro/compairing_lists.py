def compare_List(list_one,list_two):
    x = len(list_one)
    y = len(list_two)
    z = 0
    if x != y:
        print "The lists are not the same"
        
    elif x==y:
        for count in range (0,x):
            if list_one[count] == list_two[count]:
                z = z + 1
            elif list_one[count]!= list_two[count]:
                z = z + 0
        if z == x:
            print "The lists are the same"
        elif z != x:
            print "The lists are not the same"
                    
        

list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]
compare_List(list_one,list_two)

list_one = [1,2,5,6,5]
list_two = [1,2,5,6,5,3]
compare_List(list_one,list_two)

list_one = [1,2,5,6,5,16]
list_two = [1,2,5,6,5]
compare_List(list_one,list_two)

list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']
compare_List(list_one,list_two)

list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','milk']
compare_List(list_one,list_two)