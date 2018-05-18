def find_characters(str_list,char):
    x = len(str_list)
    new_list = []
    for count in range(0,x):
        y = str_list[count]
        z = len(y)
        zz = count
        for count in range(0,z):
            if y[count] == char:
                new_list.append(str_list[zz])
                break
        
    print new_list

word_list = ['hello','world','my','name','is','Anna','onomonpia']
char = 'o'
find_characters(word_list,char)