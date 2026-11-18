class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxSize = -float('inf')
        substring = set()
        l = 0

        for r in range(len(s)):
            while s[r] in substring:
                substring.remove(s[l])
                l +=1
            

            substring.add(s[r])
            maxSize = max(maxSize, len(substring))
        
        return maxSize if maxSize!= float('-inf') else 0
        