var arrangeCoins = function(n) {
    let remaining = n;
    let count = 0;
    
    for (let i = 1; remaining >= i; i++) {
        remaining -= i;
        count++;
    }
    
    return count;
};