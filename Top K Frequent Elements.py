class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}

        for num in nums:
            if num in count_dict:
                count_dict[num] +=1
            else:
                count_dict[num] = 1
        print(sorted(count_dict.items()))
        x = sorted(count_dict.items(), key=lambda item: item[1], reverse=True)
        top_k = [item[0] for item in x[:k]]
        return top_k