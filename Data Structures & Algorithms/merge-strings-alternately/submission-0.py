class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        i = 0
        j = 0
        while i < len(word1) and j < len(word2):
            res += word1[i]
            res += word2[j]
            i += 1
            j += 1
        
        # add leftover from word1
        if i < len(word1):
            res += word1[i:]

        # add leftover from word2
        if j < len(word2):
            res += word2[j:]

        return res
        