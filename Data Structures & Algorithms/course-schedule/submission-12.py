class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
       
        adjlist = {i:[] for i in range(numCourses)}

        for crs ,pre in prerequisites:
            adjlist[crs].append(pre)


        visited = set()

        def dfs(crs):
            if crs in visited:
                return False

            # visited.add(crs)

            if adjlist[crs] == []:
                return True
        #most imp
        # You only add a course to the path when it still has prerequisites to check.
            visited.add(crs)

            for pre in adjlist[crs]:
                if not dfs(pre):
                    return False

            visited.remove(crs)
            adjlist[crs] = []
            return True


        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True




