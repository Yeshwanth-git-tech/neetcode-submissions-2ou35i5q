class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]

        carry = 1
        i = 0
        while carry:
            if i < len(digits):
                # if digits[i] == "9":
                if digits[i] == 9:
                    #carry =1
                    digits[i] = 0
                else:
                    digits[i]+=1
                    carry = 0
                #i forgot to increment i
                i+=1

            else:
                digits.append(1)
                carry = 0
                
        return digits[::-1]