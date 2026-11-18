class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {']': '[', '}':'{', ')': '('}
        stack = [] # to store the opening of the parenthesis

        for each in s:
            opening = pairs.get(each)
            if stack and stack[-1] == opening:
                stack.pop()
            
            else:
                stack.append(each)


        
        return not stack
            


        