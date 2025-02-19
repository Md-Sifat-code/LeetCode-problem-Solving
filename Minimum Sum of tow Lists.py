class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        set1 = set(list1)
        set2 = set(list2)
        common_sets = list(set1 & set2)
        d={}
        for i in common_sets:
            d[i] = list1.index(i) + list2.index(i)
        
        minidex = min(d.values())
        output = []

        for i in d:
            if d[i] == minidex:
                output.append(i)

        return output