class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        line1, line2, line3 = "qwertyuiop", "asdfghjkl", "zxcvbnm"
        valid_words = []

        for word in words:
            lower_word = word.lower()

            # Check if all characters in `lower_word` are in one of the lines
            if all(char in line1 for char in lower_word) or \
               all(char in line2 for char in lower_word) or \
               all(char in line3 for char in lower_word):
                valid_words.append(word)

        return valid_words
