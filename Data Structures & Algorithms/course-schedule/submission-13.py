class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjlist = {i:[] for i in range(numCourses)}

        for crs , pre in prerequisites:
            adjlist[crs].append(pre)

        visited = set()

        def dfs(crs):
            if crs in visited:
                return False

            if adjlist[crs] == []:
                return True

            visited.add(crs)

            for nei in adjlist[crs]:
                if not dfs(nei):
                    return False
            
            adjlist[crs] = []
            visited.remove(crs)
            return True


        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True



        