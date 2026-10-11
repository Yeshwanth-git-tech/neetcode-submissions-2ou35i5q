class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {")":"(" , "}":"{" , "]":"["}

        for c in s:
            #if it is closing paranthesis
            if c in brackets:
                if stack and stack[-1] == brackets[c]:
                    stack.pop()
                else:
                    #this one condtion i was struggling
                    return False
            #and this should be in else
            else:
                stack.append(c)
            
        return True if not stack else False

   
        