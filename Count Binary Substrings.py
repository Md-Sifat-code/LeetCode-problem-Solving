class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ans , curr, prev = 0,1,0
        for i in range(1,len(s)):
            if s[i-1] != s[i]:
                ans += min(prev, curr)
                prev, curr = curr , 1
                print(prev,curr)
            else:
                curr +=1
        return ans + min(prev , curr)