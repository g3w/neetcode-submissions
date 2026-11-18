class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        maxlength = float('-inf')
        substring = set()

        for i in range(len(s)):
            while s[i] in substring:
                substring.remove(s[l])
                l += 1
            
            substring.add(s[i])
            maxlength = max(maxlength, len(substring))
    
        return maxlength if maxlength != float('-inf') else 0