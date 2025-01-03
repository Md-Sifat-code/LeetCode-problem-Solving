class Solution(object):
    def areOccurrencesEqual(self, s):
        my_list = list(s)
        letter_total = []
        for i in my_list:
            count = my_list.count(i)
            letter_total.append(count)

        set_of_total_counts = set(letter_total)
        n = len(set_of_total_counts)
        if n == 1:
            return True
        else:
            return False
