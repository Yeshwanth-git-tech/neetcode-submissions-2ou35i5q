class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF

        while (b&mask) > 0:
            carry = (a & b) << 1 # so we and and shift ti           
            a = a^b
            b = carry

        if b > 0:
            return a&mask
        else:
            return a
