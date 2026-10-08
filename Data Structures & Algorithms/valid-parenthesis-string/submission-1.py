class Solution:
    def checkValidString(self, s: str) -> bool:
        leftmin = 0
        leftmax = 0


        for char in s:
            if char == "(":
                leftmin+=1
                leftmax+=1
            elif char == ")":
                leftmin-=1
                leftmax-=1

            else:
                leftmin-=1
                leftmax+=1
            
            if leftmax <0:
                return False

            if leftmin<0:
                leftmin = 0

        return leftmin == 0
