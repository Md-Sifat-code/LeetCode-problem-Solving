class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        if len(nums)<3:
            return nums[-1]
        else:
            x = nums[-3]
            return x