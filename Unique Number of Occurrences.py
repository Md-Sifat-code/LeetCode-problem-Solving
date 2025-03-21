class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        extra = []
        for i in range(len(arr)):
            
            if arr[i] not in arr[:i]:
                count = 0
                for j in range(len(arr)):
                    if arr[i] == arr[j]:
                        count += 1
                extra.append(count)
        
        x = set(extra)
        return len(x) == len(extra)
