class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c:set() for w in words for c in w}

        for i in range(len(words)-1):
            w1 , w2 = words[i] , words[i+1]

            minlen = min(len(w1) , len(w2))

            if len(w1) > len(w2) and w1[:minlen] == w2[:minlen]:
                return ""

            
            for j in range(minlen):
                if w1[j]!=w2[j]:
                    adj[w1[j]].add(w2[j])
                    #dont forget to break
                    break

        #to detect loop
        path = set()
        #to avoid duplicates
        visited = set()

        res = []


        def dfs(c):
            if c in path:
                return True

            # Returning early from visit does both: no duplicate in res, and no wasted recursive calls.
                
            if c in visited:
                return False

            path.add(c)
            for neighbor in adj[c]:
                if dfs(neighbor):
                    return True
                    #if return True , it is a loop , if it return false , it is already visited , we will remove it from path and add it to visited
            path.remove(c)
            visited.add(c)

            res.append(c)

            return False


        for c in adj:
            #if it is True we have detected a cycle
            if dfs(c):
                return ""

        res.reverse()
        print("".join(res))
        
        return "".join(res)
        