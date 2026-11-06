class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)) + "#" + s)
        print(res)
        print("".join(res))
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        # data = s.split()
        res = []
        i = 0

        while i<len(s):
            j = i
            # while j!="#":
            while s[j]!="#":
                j+=1
            
            length = int(s[i:j])
            word = s[j+1:j+1+length]
            res.append(word)
            i = j+1+length
    
        return res

