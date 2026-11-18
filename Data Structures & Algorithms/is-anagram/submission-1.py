class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}

        for char in s:
            s_dict[char] = s_dict.get(char, 0) + 1

        
        for char in t:
            s_dict[char] = s_dict.get(char, 0) - 1

        
        for count in s_dict.values():
            if count != 0:
                return False
        
        return True