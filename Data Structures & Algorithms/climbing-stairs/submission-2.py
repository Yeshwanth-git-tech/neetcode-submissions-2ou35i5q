class Solution:
    def climbStairs(self, n: int) -> int:
        one = 1 
        two = 1

        for i in range(n-1 , 0 , -1):
            print(i)
            temp = one + two
            one  = two
            two = temp

        return two
        