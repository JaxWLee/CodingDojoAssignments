var q = 40;
var w = 200;
var x = random_chance(q,w);
console.log(x);
function random_chance(q,w){
    for (var i = q; i >= 0; i--){
        var chance = Math.floor((Math.random()*100))+1;
        if (chance==5){
            i = i + Math.floor((Math.random()*50))+50;
            if (i >= w || w == undefined){
            return i;
            }
        }
        else if (i == 0){
            return i;
        }
    }
}