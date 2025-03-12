class Solution(object):
    def singleNonDuplicate(self, nums):
        count_dict = {}
        for num in nums:
            if num in count_dict:
                count_dict[num] +=1
            else:
                count_dict[num] = 1
        result = [key for key,count in count_dict.items() if count == 1]
        return result[0]