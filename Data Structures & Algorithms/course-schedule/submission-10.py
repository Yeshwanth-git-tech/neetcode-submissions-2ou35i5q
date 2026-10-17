class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # preMap = {}
        # for i in range(numCourses):
        #     preMap[i] = []
        preMap = {i:[] for i in range(numCourses)}

        for crs , pre in prerequisites:
            preMap[crs].append(pre)

        visited = set()

        def dfs(crs):
            if crs in visited:
                return False

            if preMap[crs] == []:
                return True

            visited.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            preMap[crs] = []

            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
        
#         Time: O(V + E), where V = numCourses and E = len(prerequisites). Each course is fully explored once, and each prerequisite edge is checked once.
# Space: O(V + E) for preMap, plus O(V) for the path set and recursion stack.



        