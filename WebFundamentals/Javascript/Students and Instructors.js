var students = [ 
    {first_name:  'Michael', last_name : 'Jordan'},
    {first_name : 'John', last_name : 'Rosales'},
    {first_name : 'Mark', last_name : 'Guillen'},
    {first_name : 'KB', last_name : 'Tonel'}
];
var n = students.length;
for (var i = 0; i<n; i++){
   console.log(students[i].first_name, students[i].last_name)
}

var users = {
    Students: [ 
        {first_name:  'Michael', last_name : 'Jordan'},
        {first_name : 'John', last_name : 'Rosales'},
        {first_name : 'Mark', last_name : 'Guillen'},
        {first_name : 'KB', last_name : 'Tonel'}
     ],
    Instructors: [
        {first_name : 'Michael', last_name : 'Choi'},
        {first_name : 'Martin', last_name : 'Puryear'}
     ]
    }
    var n = users.Students.length;
    var m = users.Instructors.length;
    console.log("Students:");
    for (var i = 0; i<n;i++){
        var str = users.Students[i].first_name + users.Students[i].last_name;
        var length = str.length;
        console.log(i+1,'-',users.Students[i].first_name,users.Students[i].last_name,'-',length)
    }
    console.log("Instructors:")
    for (var i = 0; i<m;i++){
        var str = users.Instructors[i].first_name + users.Instructors[i].last_name;
        var length = str.length;
        console.log(i+1,'-',users.Instructors[i].first_name,users.Instructors[i].last_name,'-',length)
    }