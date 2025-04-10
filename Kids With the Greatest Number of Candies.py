class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        output = []
        for baby in candies:
            if baby + extraCandies >= max(candies):
                output.append(True)
            else:
                output.append(False)
        return output