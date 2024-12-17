class Solution(object):
    def isLongPressedName(self, name, typed):
        i = 0  # Pointer for 'name'
        j = 0  # Pointer for 'typed'
        
        while j < len(typed):
            if i < len(name) and name[i] == typed[j]:
                # If characters match, move both pointers
                i += 1
                j += 1
            elif j > 0 and typed[j] == typed[j - 1]:
                # Allow long-pressed character in 'typed'
                j += 1
            else:
                # If it's neither a match nor a valid long-press
                return False
        
        # Ensure all characters in 'name' have been matched
        return i == len(name)
