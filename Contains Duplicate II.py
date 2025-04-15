class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        for i , al in enumerate(nums):
            if al in dic and i - dic[al] <=k:
                return True
            dic[al] = i
        return False