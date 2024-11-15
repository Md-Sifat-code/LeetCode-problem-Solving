from collections import Counter
from typing import List

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        # Extract only the letters from licensePlate and convert them to lowercase
        extra = [char.lower() for char in licensePlate if char.isalpha()]
        
        # Count the frequency of each letter in extra
        extra_count = Counter(extra)
        
        # Initialize the shortest completing word
        shortest_word = None
        
        for word in words:
            # Count the frequency of each letter in the current word
            word_count = Counter(word)
            
            # Check if the word contains all letters from extra with the required frequency
            if all(word_count[char] >= count for char, count in extra_count.items()):
                # Update the shortest_word if it's either None or the current word is shorter
                if shortest_word is None or len(word) < len(shortest_word):
                    shortest_word = word
        
        return shortest_word
