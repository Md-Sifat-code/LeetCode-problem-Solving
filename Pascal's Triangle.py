class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascaltree = []
        row = []
        for i in range(numRows):
            row = []
            for j in range(i+1):
                if j == 0  or j == i:
                    row.append(1)
                else:
                    pre_row = pascaltree[i-1]
                    row.append(pre_row[j] + pre_row[j-1])
            pascaltree.append(row)
        return pascaltree