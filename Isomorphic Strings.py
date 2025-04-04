class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Dictionaries to store the first occurrence index of each character
        char_index_s = {}
        char_index_t = {}
        
        print("Initial dictionaries:")
        print("char_index_s:", char_index_s)
        print("char_index_t:", char_index_t)
        
        # Loop through each character index in both strings
        for i in range(len(s)):
            print(f"\nIteration {i}:")
            print(f"Comparing s[{i}] = {s[i]} with t[{i}] = {t[i]}")
            
            # If the character from string s has not been encountered before
            if s[i] not in char_index_s:
                char_index_s[s[i]] = i  # Store the index of the character in s
                print(f"Character '{s[i]}' not seen before in s, storing index {i}")
            
            # If the character from string t has not been encountered before
            if t[i] not in char_index_t:
                char_index_t[t[i]] = i  # Store the index of the character in t
                print(f"Character '{t[i]}' not seen before in t, storing index {i}")
            
            # Check if the relative positions of characters from s and t match
            if char_index_s[s[i]] != char_index_t[t[i]]:
                print(f"Position mismatch: char_index_s[{s[i]}] = {char_index_s[s[i]]} and char_index_t[{t[i]}] = {char_index_t[t[i]]}")
                return False  # If the positions don't match, return False
            
            print(f"Positions match for characters '{s[i]}' and '{t[i]}':")
            print(f"char_index_s[{s[i]}] = {char_index_s[s[i]]}, char_index_t[{t[i]}] = {char_index_t[t[i]]}")
        
        # If we complete the loop without returning False, the strings are isomorphic
        print("\nStrings are isomorphic.")
        return True

