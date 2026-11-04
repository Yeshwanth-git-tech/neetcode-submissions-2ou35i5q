class Solution:
    def isHappy(self, n: int) -> bool:

        seen = set()

        while n not in seen:
            seen.add(n)
            n = self.sqaure_num(n)
            if n == 1:
                return True
                
        return False
                

    def sqaure_num(self , num):
        output = 0

        while num:
            s = num%10
            output += s*s
            num = num //10
        return output        