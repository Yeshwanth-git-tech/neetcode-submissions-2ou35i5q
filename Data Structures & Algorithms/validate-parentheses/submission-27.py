class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        closepar = {")":"(" , "]":"[" , "}":"{"}

        for char in s:
            #if this is closing paranthesis
            if char in closepar:
                if stack and stack[-1] == closepar[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return True if not stack else False