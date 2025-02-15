class Solution(object):
    def containsDuplicate(self, nums):
        
        if len(set(nums)) == len(nums):
            return False
        else:
            return True