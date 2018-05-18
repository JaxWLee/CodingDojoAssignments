def make_dict(list_1,list_2):
    new_dict={}
    x = len(list_1)
    y = len(list_2)
    if x > y:
        z = x - y
        for i in range (0,z):
            list_2.append('')
        for i in range (0,x):
            new_dict[list_1[i]] = list_2[i]
    
    elif y > x:
        z = y - x
        for i in range (0,z):
            list_1.append('')
        for i in range (0,y):
            new_dict[list_2[i]] = list_1[i]
    else:
        for i in range (0,x):
            new_dict[list_1[i]] = list_2[i]
    return new_dict

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

y = make_dict(name,favorite_animal)
print(y)