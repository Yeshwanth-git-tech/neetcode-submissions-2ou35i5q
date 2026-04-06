class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            bit = n & 1
            #shift left with the bit value , indefault it would have added 0
            #here we are adding bit 
            #so initially 0 
            # 1101 & 1 = 1 = bit 
            #0 << 1 | 1 -> 01
            res = res << 1 | bit 
            #now 1 is completed , and shift right , so hat n is 110 , basically shifting 
            n = n >> 1

        return res
        ##time complecxity O(1) and space same