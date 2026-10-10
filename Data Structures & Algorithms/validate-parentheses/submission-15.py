class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {")":"(" , "}":"{" , "]":"["}

        for c in s:
            if c in brackets:
                if not stack or stack[-1]!=brackets[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)

        return not stack

        # for char in s:
        #     if char in brackets and stack and brackets[char] == stack[-1]:
        #         stack.pop()
        #         # continue
        #     else:
        #         stack.append(char)

        # print(stack)
        # if not stack:
        #     return True
        # else:
        #     return False
        