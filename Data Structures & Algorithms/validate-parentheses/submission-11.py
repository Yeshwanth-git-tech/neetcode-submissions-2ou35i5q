class Solution:
    def isValid(self, s: str) -> bool:
        par = {'}':'{',']':'[',')':'('}
        stack = []

        for i in s:
            if i in par:
                if stack and stack[-1] == par[i]:
                    stack.pop()
                else:
                    # stack.append(i)
                    #we return false when there is no closing paranthesis 
                    #if there is opening then there must be closing paranthesis
                    return False
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
        