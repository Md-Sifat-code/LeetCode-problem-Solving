var reverse = function(x) {
    const MAX_INT = 2147483647;
    const MIN_INT = -2147483648;
    const reversed = parseInt(x.toString().split('').reverse().join(''));
    if (reversed < MIN_INT || reversed > MAX_INT) {
        return 0;
    }else{
        return Math.sign(x)*reversed;

    }

    
};