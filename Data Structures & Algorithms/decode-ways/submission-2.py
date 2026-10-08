class Solution:
    def numDecodings(self, s: str) -> int:
        one = 1
        two = 0

        for i in range(len(s)-1 , -1 , -1):
            if s[i] == "0":
                curr = 0
            else:
                curr = one
            if (i+1) < len(s) and (s[i] == "1" or s[i] == "2" and s[i+1] in "0123456"):
                curr = curr+two
            two = one
            one = curr

        return one

        