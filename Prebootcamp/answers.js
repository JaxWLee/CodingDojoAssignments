//Chapter 1 Fundamentals 
// Setting and Swapping
myNumber = 42;
myName='Jaxon';
[myNumber, myName] = [myName, myNumber]
console.log(myName,myNumber)

//Print -52 to 1066
for (i = -52; i < 1067; i++){
    console.log(i);
}

//Don't Worry, Be Happy
function beCheerful( )
{
    console.log("good morning!")
    
}
for (i = 1; i < 99; i++){
    beCheerful();
}

//Multiples of Three -- but Not All
for (i = -300;i <= 0; i = i+3)
{
    if (i == -3 || i == -6){
        continue;
    }
    console.log(i)
}

//Printing Intergers with While
i = 2000;
while (i<=5280)
{
    console.log(i)
    i += 1
}

//You Say It's Your Birthday

function birthday(x,y)
{
    if ([x,y] == [7,9] || [x,y] == [9,7])
    {
        console.log("How did you know?")

    }
    else 
    {
        console.log('Just another day...')
    }
}
//Leap Year
function leapyear(year)
{
    if (year % 100 == 0 && year % 400 !== 0)
        {
            console.log(year + ' is not a leap year')
        }
    if (year % 4 == 0)
    {
    
        console.log(year + ' is a leap year' )
    }
    else
    {
        console.log(year + ' is not a leap year')
    }
}
leapyear(2000);
leapyear(400);
leapyear(100);

