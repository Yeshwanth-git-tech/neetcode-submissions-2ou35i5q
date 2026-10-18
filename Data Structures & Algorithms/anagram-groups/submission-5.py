class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #so we are going to use the index as count 
        groups = defaultdict(list)
        #so key is the where the count of each str are there
        #so for each for str , we will have the count bycjert

        #and use that count bucket as the key

        for s in strs:
            count = [0]*26 #0-25
            for c in s:
                #ord a 97 , if c == a , then count[0]+=1
                count[ord(c) - ord("a")]+=1

            key = tuple(count)

            groups[key].append(s)

        res = [values for values in groups.values()]

        return res




        
        