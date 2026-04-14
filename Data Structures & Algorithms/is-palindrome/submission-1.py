class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = ""
        for c in s:
            if c.isalnum():
                #dont forget to lowercase
                ss+=c.lower()
        return ss == ss[::-1]
        