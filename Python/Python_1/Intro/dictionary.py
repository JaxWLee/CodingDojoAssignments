dictionary ={
    'first name': 'Jaxon',
    'last name': 'Lee',
    'country of origin': 'USA',
    'favorite language': 'Python'
}
def unpack_dictionary(dictionary):
    for key in dictionary:
        value = dictionary[key]
        print "My "+str(key)+" is "+str(value)
unpack_dictionary(dictionary)

