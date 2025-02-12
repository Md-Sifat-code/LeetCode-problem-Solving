class Solution(object):
    def gcdOfStrings(self, str1, str2):
        unique_string_1= ''.join(OrderedDict.fromkeys((str1)))
        unique_string_2= ''.join(OrderedDict.fromkeys((str2)))
        if unique_string_1 == unique_string_2:
            return unique_string_1
        else:
            return ""