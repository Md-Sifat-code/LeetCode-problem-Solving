class Solution(object):
    def reverseWords(self, s):
        words = s.split()
        n = len(words)-1
        for i in range((n+1)//2):
            temp = words[i]
            words[i] = words[n-i]
            words[n-i] = temp
        
        return ' '.join(words)