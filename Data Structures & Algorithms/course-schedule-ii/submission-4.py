class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i:[] for i in range(numCourses)}


        for crs, pre in prerequisites:
            adj[crs].append(pre)

        
        visited = set()

        path = set()

        res = []

        def dfs(c):
            if c in path:
                return False

            if c in visited:
                return True

            path.add(c)
            for nei in adj[c]:
                if not dfs(nei):
                    return False     
            path.remove(c)
            visited.add(c)
            res.append(c)  
            return True


        

        for c in range(numCourses):
            if not dfs(c):
                return []
        return res
