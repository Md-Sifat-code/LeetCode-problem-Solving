class Solution(object):
    def pivotIndex(self, nums):
        
        for i in range(len(nums)):
            left_side = sum(nums[:i])
            right_side = sum(nums[i+1:])
            if left_side == right_side:
                return i
            
        return -1