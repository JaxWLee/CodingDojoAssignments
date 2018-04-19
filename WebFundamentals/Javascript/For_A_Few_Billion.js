var start = 0.01;
var days = 0;
for (i=1;i<=30; i++){
    start = start*2;
    if (start>=10000){
        days = i;
        console.log(days)
    }
}
console.log('After 30 days we have $',start);
console.log('After 20 days we have more than $10,000')

var i = 1;
start = 0.01;
while (start<=1000000000){
    start = start*2;
    i = i+1;
}
console.log('It takes', i, 'days to have a billion dollars')

i=1;
start = 0.01;
while (start<=Infinity){
    start = start*2;
    i = i+1;
    if (start==Infinity){
        break;
    }
}
console.log('It takes', i, 'days to have infinite money.')