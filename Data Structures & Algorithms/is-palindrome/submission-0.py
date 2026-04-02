class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = "".join([c.lower() for c in s if c.isalnum()])

        # print(ss)

        # l, r= 0 , len(ss)-1

        # if s == s[::-1]:
        #     return True
        # else:
        #     return False

        l,r = 0, len(s)-1

        while l < r:
            while l < r and  not self.alphanumerical(s[l]):
                l+=1
            while r > l  and not self.alphanumerical(s[r]):
                r-=1
            if s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1
        return True

    def alphanumerical(self,c):
        return (ord("A") <= ord(c) <=ord("Z") or 
                ord("a") <= ord(c) <=ord("z") or 
                ord("0") <= ord(c) <=ord("9"))