class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}
        def solve(i, j):
            #Delete all the remaining chars in the String 1
            if j == len(word2):
                return len(word1) - i
            #Insert all the remaining characters to String 1
            elif i == len(word1):
                return len(word2) - j
            if (i, j) in dp:
                return dp[(i, j)]
            #If chars from both strings match
            if word1[i] == word2[j]:
                dp[(i, j)] = solve(i+1, j+1)
                return dp[(i, j)]
            dp[(i, j)] = 1 + min(
                solve(i, j+1), #Insertion
                solve(i+1, j), #Deletion
                solve(i+1, j+1)) #Replace
            return dp[(i, j)]
        return solve(0, 0)