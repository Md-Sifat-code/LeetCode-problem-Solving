var missingNumber = function(nums) {
    let numbers = new Set(nums);
    let n = nums.length;
    
    for(let i = 0; i < n; i++){
        if(!numbers.has(i)) return i;
    }
    
    return n;
};