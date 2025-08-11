class Solution:
    def equalPairs(self, grid):
        n = len(grid)
        count = 0
        for i in range(n):
            for j in range(n):
                flag = True
                for k in range(n):
                    if grid[i][k] != grid[k][j]:
                        flag = False
                        break
                if flag:
                    count += 1
        return count
