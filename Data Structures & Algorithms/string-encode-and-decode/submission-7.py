class Solution:

    def encode(self, strs: List[str]) -> str:
        # res = " "

        # for s in strs:
        #     l = len(s)
        #     res+= str(l) + "#" + s
        # print(res)
        # return res O(m) square as strings are immutable

        res = []

        for s in strs:
            l = len(s)
            new_str = str(l) + "#" + s

            res.append(new_str)

        return "".join(res)

        #amortized O(m) time complexity

        #space complexity 

        #O(m) space and O(m) time both encode and decode
        #no brute force for these and all 


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            # while j!= "#":
            #see the above will cause infinite loop
            #it is s[j]
            while s[j]!="#":
                j+=1
            length = int(s[i:j])
            word = s[j+1:j+1+length]
            # print(word)
            res.append(word)
            #increment i
            i = j+1+length
        #     print(i)

        return res



        
