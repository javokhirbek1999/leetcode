/**
 * @param {number} x
 * @param {number} y
 * @param {number} bound
 * @return {number[]}
 */
var powerfulIntegers = function(x, y, bound) {
    var p = [];
    for(var i = 0; i<20; i++){
        for(var j = 0; j<20; j++){
            var t = Math.pow(x,i)+Math.pow(y,j);
            if(t<=bound && !p.includes(t)){
                p.push(t);
            }
        }
    }
    p.sort(function(a,b){return a-b});
    return p;
};
