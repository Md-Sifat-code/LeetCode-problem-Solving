from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        anargam_map = defaultdict(list)
        result = []
        for s in strs:
            sorted_s = tuple(sorted(s))
            anargam_map[sorted_s].append(s)
        
        for values in anargam_map.values():
            result.append(values)
        
        return result