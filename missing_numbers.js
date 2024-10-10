var missingNumber = function(nums) {
    let n = nums.length;
    for (let i = 0; i <= n; i++) {
        let found = false;
        for (let j = 0; j < nums.length; j++) {
            if (i === nums[j]) {
                found = true;
                break;
            }
        }
        if (!found) {
            return i;
        }
    }
};