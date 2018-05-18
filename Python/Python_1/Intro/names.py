users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

x = len(users)
s = len(users['Students'])
I = len(users['Instructors'])
for i in range (0,x):
    if i == 0:
        print 'Students:'
        for n in range(0,s):
            y = users['Students'][n]['first_name'] + ' ' +users['Students'][n]['last_name']
            z = len(y) - 1
            print n+1,'-',y,'-',z
    if i == 1:
        print 'Instructors:'
        for n in range(0,I):
            y = users['Instructors'][n]['first_name'] + ' ' +users['Instructors'][n]['last_name']
            z = len(y) - 1
            print n+1,'-',y,'-',z