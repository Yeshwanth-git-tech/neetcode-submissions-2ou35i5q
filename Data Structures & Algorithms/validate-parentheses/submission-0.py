class Solution:
    def isValid(self, s: str) -> bool:
        par = {"}":"{", "]":"[", ")":"("}

        stack = []

        for c in s:
            # if the key , that is closing paranthesis in hashmap
            if c in par:
                if stack and stack[-1] == par[c]:
                    stack.pop()
                else:
                    return False

            else:
                #if the stack is opening parantheses
                stack.append(c)

        return True if not stack else False