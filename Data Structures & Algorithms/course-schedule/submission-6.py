class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hashmap = {i:[] for i in range(numCourses)}

        for crs , pre in prerequisites:
            hashmap[crs].append(pre)

        visit = set()

        def dfs(crs):
            if crs in visit:
                return False
            
            if hashmap[crs] == []:
                return True
            
            visit.add(crs)

            for pre in hashmap[crs]:
                if not dfs(pre):return False
            #this we are doing to avoid false positive
            visit.remove(crs)
            # hashmap[crs] == []
            #be carefull while typing
            hashmap[crs] = []

            return True

        for crs in range(numCourses):
            if not dfs(crs): 
                return False
        
        return True




