class Solution:
    def checkValidString(self, s: str) -> bool:
        leftmin = 0
        leftmax = 0

        for i in range(len(s)):
            if s[i] == "(":
                leftmax +=1
                leftmin +=1
            elif s[i] == ")":
                leftmin -=1
                leftmax -=1
            else:
                #"*"
                leftmin -=1
                leftmax +=1
            if leftmax<0:
                return False
            if leftmin<0:
                leftmin=0
        return leftmin == 0
        