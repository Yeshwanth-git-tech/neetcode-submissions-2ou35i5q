class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = defaultdict(list)

        
        for s in strs:
            #this will be used as key
            count = [0] *26
            for w in s:
                count[ord(w) - ord("a")]+=1
            key = tuple(count)
            groups[key].append(s)

        return list(groups.values())


        
        