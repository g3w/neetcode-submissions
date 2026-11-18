class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {']': '[', '}':'{', ')': '('}
        stack = [] # to store the opening of the parenthesis

        for i in s:
            #if i in pairs:
            opening = pairs.get(i)

            if stack and stack[-1] == opening:
                stack.pop()                
            else:
                stack.append(i)
        
        return not stack
            


        