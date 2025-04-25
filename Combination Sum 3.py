class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        output = []
        def okay(build,num, sum_so_far):
            if len(build) == k:
                if sum_so_far == n : output.append(build)
                return
            for i in range(num,9+1):
                if sum_so_far+i > n: break
                okay(build+[i], i+1, sum_so_far +i)
        
        okay([],1,0)
        return output