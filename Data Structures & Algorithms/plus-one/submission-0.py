class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        i = 0

        #first reverse since we add from the end , thats one place

        digits = digits[::-1]

        print(digits)



        while carry:
            if i < len(digits):
                if digits[i] == 9:
                    print(True)
                    #make it zero
                    digits[i] = 0
                    #carry is still one  , we dont need to channge anything
                    #you for got to incremetn
                else:
                    digits[i]+=1
                    carry = 0
                i+=1

            else:
                #still we are in bounf
                #and carry is still one
                digits.append(1)
                carry = 0

        print("dd" , digits)
        
        return digits[::-1]