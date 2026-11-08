class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i:[] for i in range(numCourses)}


        for crs , pre in prerequisites:
            adj[crs].append(pre)

        
        visited = set()

        def dfs(c):
            if c in visited:
                return False
            
            if adj[c] == []:
                return True
            
            visited.add(c)

            for nei in adj[c]:
                if not dfs(nei):
                   return False
            visited.remove(c)
            adj[c] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        # return True if len(visited) == numCourses else False
        # return len(visited) == numCourses 
        return True


            