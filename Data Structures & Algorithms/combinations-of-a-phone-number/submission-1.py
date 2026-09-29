class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
                    }

        def backtrack(i , currstr):
            if len(currstr) == len(digits):
                res.append(currstr)
                return

            
            for c in digitToChar[digits[i]]:
                backtrack(i+1 , currstr+c)

                # No pop() needed. curStr + c creates a new string for each call, so curStr in the parent never changes. That's different from Subsets, where one shared list was modified and had to be undone.

        
        if digits:
            backtrack(0 , "")

        return res

        