/**
 * @param {number} x
 * @param {number} n
 * @return {number}
 */
var myPow = function(x, n) {
    return recPow(x,n);
};


var recPow = (x,n)=>{
    if (n === 0 || x === 1) return 1;

    if(n<0){
        return 1/recPow(x,-n);
    }

    if(n%2===1){
        return x*recPow(x,n-1);
    }else{
        return recPow(x*x,n/2)
    }
}