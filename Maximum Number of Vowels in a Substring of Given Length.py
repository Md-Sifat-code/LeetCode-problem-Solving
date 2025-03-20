class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        chunks = []
        numbers = []
        for i in range(0, len(s), k):
            chunks.append(s[i:i+k])
        print(chunks)
        
        for i in range(len(chunks)):
            count = 0
            for elements in chunks[i]:
                if elements == "a" or elements == "e" or elements == "i" or elements == "o" or elements == "u":
                    count +=1
                    
            numbers.append(count)
        return max(numbers)

