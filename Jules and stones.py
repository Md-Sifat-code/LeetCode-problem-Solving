class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # Convert jewels to a set for faster lookup
        jewel_set = set(jewels)
        
        # Initialize the counter
        count = 0
        
        # Iterate through each stone and check if it's a jewel
        for stone in stones:
            if stone in jewel_set:
                count += 1
                
        return count
