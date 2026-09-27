class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        premap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            premap[crs].append(pre)

        visited = set()
        output = []
        cycle = set()

        def dfs(crs):
            if crs in cycle:
                return False

            if crs in visited:
                return True

            cycle.add(crs)
            for pre in premap[crs]:
                if not dfs(pre):
                    return False

            cycle.remove(crs)
            # premap[crs] = []
            visited.add(crs)
            output.append(crs)
            return True   


        # state = [0] * numCourses   # 0 = unvisited, 1 = visiting, 2 = done

        # def dfs(crs):
        #     if state[crs] == 1:
        #         return False
        #     if state[crs] == 2:
        #         return True

        #     state[crs] = 1
        #     for pre in premap[crs]:
        #         if not dfs(pre):
        #             return False
        #     state[crs] = 2
        #     output.append(crs)
        #     return True   



        for crs in range(numCourses):
            if not dfs(crs):
                return []

        return output  