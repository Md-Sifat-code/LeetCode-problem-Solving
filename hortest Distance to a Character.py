class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        extra =[]
        for i in range(0,len(s)):
            if s[i] == c:
                extra.append(i)
        output =[]
        for j in range(0,len(s)):
            low = float('inf')
            for k in range(0,len(extra)):
                result = abs(extra[k]-j)
                if result <low:
                    low = result
            
            output.append(low)


        return output

