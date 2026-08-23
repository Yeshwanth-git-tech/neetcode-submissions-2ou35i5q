class Solution:

    def encode(self, strs: List[str]) -> str:
        newlist = []

        for s in strs:
            newlist.append(str(len(s)) + "#" + s)
        res =  "".join(newlist)
        return res
        

    def decode(self, s: str) -> List[str]:
        
        #lets start with getting the length
        newlist = []
        i = 0
        while i < len(s):
            j = i
            while s[j]!= "#":
            # while j!= "#":
                #finding the length
                j+=1
            length = int(s[i:j])
            newlist.append(s[j+1:j+1+length])
            i = j+1+length

        return newlist


