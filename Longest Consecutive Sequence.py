class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longestS = 0

        num_set = set(nums)
        for n in num_set:
            if (n-1) not in num_set:
                length = 1
                while (n+length) in num_set:
                    length += 1
                longestS = max(longestS,length)
        return longestS
        