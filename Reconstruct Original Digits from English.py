class Solution(object):
    def originalDigits(self, s):
        from collections import Counter
        c = Counter(s)
        d = {}
        d[0] = c['z']
        d[2] = c['w']
        d[4] = c['u']
        d[6] = c['x']
        d[8] = c['g']
        d[1] = c['o'] - d[0] - d[2] - d[4]
        d[3] = c['h'] - d[8]
        d[5] = c['f'] - d[4]
        d[7] = c['s'] - d[6]
        d[9] = c['i'] - d[5] - d[6] - d[8]
        return ''.join(str(i) * d[i] for i in range(10))