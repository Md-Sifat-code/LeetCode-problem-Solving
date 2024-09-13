var climbStairs = function(n) {
    const x = new Array(n+1).fill(0);
    x[0] =1;
    x[1] = 1;

    for(let i =2; i<=n;i++){
        x[i] = x[i-1]+ x[i-2];

    }
    return x[n];
};