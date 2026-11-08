class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        subset = []

        def backtrack(openn , close):
            if n == openn == close:
                res.append("".join(subset))
                return 

            if openn < n:
                subset.append("(")
                backtrack(openn+1 , close)
                subset.pop()
            
            if close < openn:
                subset.append(")")
                backtrack(openn , close+1)
                subset.pop()
        
        backtrack(0 , 0)
        return res