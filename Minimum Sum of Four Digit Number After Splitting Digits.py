class Solution(object):
    def minimumSum(self, num):
        num = sorted(str(num),reverse=True)
        return int(num[0]) + int(num[1]) + int(num[2])*10 + int(num[3])*10
