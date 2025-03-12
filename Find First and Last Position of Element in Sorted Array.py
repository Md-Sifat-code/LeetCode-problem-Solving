class Solution(object):
    def searchRange(self, nums, target):
        answer = [-1, -1]
        for i in range(len(nums)):
            if nums[i] == target:
                answer[0] = i
                break
        if answer[0] == -1:
            return answer
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == target:
                answer[1] = i
                break
        
        return answer
