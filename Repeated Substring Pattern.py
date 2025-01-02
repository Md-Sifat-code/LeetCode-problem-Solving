class Solution(object):
    def repeatedSubstringPattern(self, s):
        s_fold = "".join( (s[1:], s[:-1]) )
        
        return s in s_fold