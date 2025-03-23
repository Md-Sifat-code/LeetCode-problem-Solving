class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        count = 0
        previous =0
        for rung in rungs:
            if rung - previous > dist:
                count += (rung - previous - 1) // dist
            previous = rung
        
        return count

        