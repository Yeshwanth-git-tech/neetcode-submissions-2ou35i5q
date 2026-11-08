class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        chartomap = {"2":"abc",
                    "3":"def" , 
                    "4":"ghi",
                    "5":"jkl",
                    "6":"mno",
                    "7":"pqrs",
                    "8":"tuv",
                    "9":"wxyz"                    
                    }
        res = []
        def backtrack(i ,currstr):
            # if len(currstr) == len(digits):
            if i == len(digits):
                res.append(currstr)
                return 

            for s in chartomap[digits[i]]:
                backtrack(i+1 , currstr+s)
        if digits:
            backtrack(0 , "")

        return res