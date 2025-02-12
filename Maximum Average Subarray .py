class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        n=len(nums)

        window_sum = max_sum=sum(nums[:k])

        for i in range(n-k):
            window_sum = window_sum - nums[i] + nums[i+k]

            if window_sum > max_sum:
                max_sum = window_sum

        return max_sum/float(k)