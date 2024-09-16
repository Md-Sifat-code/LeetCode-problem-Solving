var isPowerOfThree = function(n) {
    while(n>1){
        n /= 3;
    }
    return n === 1
};