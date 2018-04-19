var a = [1, 4, "jill", "bill", 14, 19, 'nancy'];
var x = numbers_only(a);
console.log(x)
function numbers_only(a){
    var n = a.length;
    var new_array=[];
    for (var i=0;i<n;i++){
        if (typeof(a[i]) === "number"){
            new_array.push(a[i])
        }
    }
    return new_array;
}
