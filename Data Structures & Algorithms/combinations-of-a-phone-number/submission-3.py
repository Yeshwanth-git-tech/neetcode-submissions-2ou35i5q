class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        digitstochar = {"2":"abc",
                        "3":"def",
                        "4":"ghi",
                        "5":"jkl",
                        "6":"mno",
                        "7":"pqrs",
                        "8":"tuv",
                        "9":"wxyz"}
        res = []
        # subset = [] here you dont need subset , as this is string
        def backtrack(i , curr):
            if i == len(digits):
                res.append("".join(curr))
                return

            for char in digitstochar[digits[i]]:
                backtrack(i+1 , curr+char)


        if digits:
            backtrack(0 , "")
        return res


        
