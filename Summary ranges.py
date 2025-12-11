class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        i = 0
        
        while i < len(nums):
            start = nums[i]
            
            # find the end of the range
            while i + 1 < len(nums) and nums[i + 1] == nums[i] + 1:
                i += 1
            
            end = nums[i]
            
            if start == end:
                result.append(str(start))
            else:
                result.append(f"{start}->{end}")
            
            i += 1  # move to next number
        
        return result