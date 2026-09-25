class Solution:
    def numDecodings(self, s: str) -> int:
        one, two = 1 , 0

        for i in range(len(s)-1 , -1 , -1):
            curr = 0
            if s[i] == "0":
                curr = 0
            else:
                curr = one

            if (i+1) < len(s) and (s[i] == "1" or s[i] == "2" and s[i+1] in "0123456"):

                curr = curr + two
            two = one
            one = curr
    

        return one
        