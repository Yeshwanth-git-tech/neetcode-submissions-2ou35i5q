class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {")":"(" , "}":"{" , "]":"["}

        for char in s:
            if char in brackets and stack and brackets[char] == stack[-1]:
                stack.pop()
                # continue
            else:
                stack.append(char)

        print(stack)
        if not stack:
            return True
        else:
            return False
        