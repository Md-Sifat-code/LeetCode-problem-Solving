var search = function(nums, target) {
    let n = nums.length;
    let start =0; 
    let end = n-1;
    while(start <= end){
        let mid = Math.floor(start + (end-start)/2);
        if(nums[mid] == target){
            return mid;
        }else if(nums[mid]<= target){
            start = mid+1;
        }else{
            end = mid-1;
        }
    }
    return -1;
};