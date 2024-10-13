var intersect = function(nums1, nums2) {
    let n = nums1.length;
    let k = nums2.length;
    let array = [];
    
    if (n < k) {
        for (let i = 0; i < n; i++) {
            for (let j = 0; j < k; j++) { 
                if (nums1[i] === nums2[j]) {
                    array.push(nums1[i]);
                    nums2[j] = null;  
                    break;
                }
            }
        }
    } else {
        for (let i = 0; i < k; i++) {
            for (let j = 0; j < n; j++) {
                if (nums2[i] === nums1[j]) {
                    array.push(nums2[i]);
                    nums1[j] = null;
                    break;
                }
            }
        }
    }

    return array;
};
