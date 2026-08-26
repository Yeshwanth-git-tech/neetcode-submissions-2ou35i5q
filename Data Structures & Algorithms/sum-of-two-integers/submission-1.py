class Solution:
    def getSum(self, a: int, b: int) -> int:
        # mask = 0xFFFFFFFF 
        # # The 0x is just Python’s notation saying:
        #1F = 4 bits , 8F = 8*4= 32 bits

        # # “The number after this is written in hexadecimal (base 16).”
        # while b & mask:
        #     #since a is changed we will store it in temp
        #     temp = (a&b) << 1
        #     a = a^b
        #     #since a is changed we will store it in temp
        #     b = temp

        # #handle the negative values
        # if b == 0:
        #     return a
        # else:
        #     return ~(a ^ mask)





        mask = 0XFFFFFFFF

        while b&mask:
            temp = (a&b) << 1
            a = a^b

            b = temp

        if b==0:
            return a
        else:
            return ~(a^mask)













