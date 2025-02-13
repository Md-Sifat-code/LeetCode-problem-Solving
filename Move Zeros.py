class Solution(object):
    def moveZeroes(self, nums):
        
        npm_zero =0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[npm_zero], nums[i] = nums[i], nums[npm_zero]
                npm_zero +=1
        
        return nums
        