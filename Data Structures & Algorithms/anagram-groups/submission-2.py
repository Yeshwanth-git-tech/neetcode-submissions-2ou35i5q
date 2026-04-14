class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #base case

        #O(m (the number of string given ) * n ( average lenght of each string)*26) - O(m*n)

        #space O(n)

        # if len(strs) == 1:
        #     return list(strs)
        #key is going to be count anfstring such 1a , 1c , 1t
        # value is the string itself in a list
        hashmap = defaultdict(list)
     
        for s in strs:
            count  = [0] * 26 #a-z
            for c in s:
                count[ord(c) - ord("a")]+=1

            hashmap[tuple(count)].append(s)

        print(hashmap.values())

        return list(hashmap.values())


