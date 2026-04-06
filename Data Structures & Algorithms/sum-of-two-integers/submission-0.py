class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF 

        while b & mask:
            #since a is changed we will store it in temp
            temp = (a&b) << 1
            a = a^b
            #since a is changed we will store it in temp
            b = temp

        #handle the negative values
        if b == 0:
            return a
        else:
            return ~(a ^ mask)