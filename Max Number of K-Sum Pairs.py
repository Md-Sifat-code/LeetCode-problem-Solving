class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right = 0, len(nums)-1
        output = 0
        while left < right:
            pair_sum = nums[left] + nums[right]
            if pair_sum == k:
                output += 1
                left += 1
                right -= 1
            elif pair_sum < k:
                left += 1
            else:
                right -= 1
        return output
