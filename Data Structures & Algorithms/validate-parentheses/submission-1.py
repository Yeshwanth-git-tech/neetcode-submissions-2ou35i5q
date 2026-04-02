class Solution:
    def isValid(self, s: str) -> bool:
        par = {"}":"{", "]":"[", ")":"("}

        stack = []

        for c in s:
            if c in par:
                #if stack is not empty
                if stack and stack[-1] == par[c]:
                    stack.pop()
                else:
                    return False
            #if the paranthesis is opening        
            else:
                stack.append(c)
        
        return True if not stack else False

