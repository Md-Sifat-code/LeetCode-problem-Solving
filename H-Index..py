class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)

        citations.sort()
        for i,num in enumerate(citations):
            if n -i <= num:
                return n -i
        return 0
