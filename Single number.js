var singleNumber = function(nums) {
    
    for(let i =0; i<nums.length;i++){
        let x =0;
        for(let j =0; j<nums.length;j++){
            if(nums[i] === nums[j] ){
                x++;

            }
            
        }
        if(x<2){
            return nums[i];
        }
    }
    
};