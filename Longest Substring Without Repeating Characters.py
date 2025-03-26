class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maxlength = 0
        charSet = set()
        left = 0
        for right in range(n):
            while s[right] in charSet:
                charSet.remove(s[left])
                left+=1
            charSet.add(s[right])
            maxlength = max(maxlength, right-left +1)
        return maxlength