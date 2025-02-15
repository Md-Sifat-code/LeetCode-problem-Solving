class Solution(object):
    def findDisappearedNumbers(self, nums):
        n = len(nums)

        all_numbers = set(range(1, n+1))
        nums_set = set(nums)
        missing = list(all_numbers - nums_set)
        return missing