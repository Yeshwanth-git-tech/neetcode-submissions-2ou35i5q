class Solution:
    def isValid(self, s: str) -> bool:
        par = {'}':'{',']':'[',')':'('}
        stack = []

        for i in s:
            # we will check the clsoiing paranthesis is there in the par
            if i in par:
                if stack and stack[-1] == par[i]:
                    stack.pop()
                else:
                    return False
                #if it is opening just add
            else:
                stack.append(i)
            
        return True if not stack else False























        # for c in s:
        #     if c in par:
        #         if stack and stack[-1] == par[c]:
        #             stack.pop()
        #         else:
        #             return False
        #     else:
        #         stack.append(c)

        # return True if not stack else False
        