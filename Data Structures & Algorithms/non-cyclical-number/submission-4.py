class Solution:
    def isHappy(self, n: int) -> bool:

        seen = set()
        while n not in seen:
            seen.add(n)
            # sq = self.calculate_sqaure(n)
            n = self.calculate_sqaure(n)
            # if sq == 1:
            if n == 1:
                return True
        return False


    def calculate_sqaure(self, x):
        total = 0
        while x:
            res= x%10
            total += res*res
            x = x//10
            
        return total