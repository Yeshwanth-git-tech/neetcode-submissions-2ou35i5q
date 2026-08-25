class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hashmap = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            hashmap[crs].append(pre)

        #it will have hashmap : {1:[1 ,2 ,3]}

        #vistset to avoid loop [0 , 1], [1 , 2] , 
        #[2, 0] here it forms an infinitle loop in dfs

        visit = set()

        def dfs(crs):
            if crs in visit:
                return False
            
            if hashmap[crs] == []:
                return True

            visit.add(crs)

            for pre in hashmap[crs]:
                if not dfs(pre):return False
            #else so it is true
            #so basically we are removing this 
            #to avoid the traversing missing an 
            #valid route , so that wsy we are maling the list too empty
            visit.remove(crs)
            hashmap[crs] = []
            #then return True
            return True

        for crs in range(numCourses):
            if not dfs(crs):return False

        return True


