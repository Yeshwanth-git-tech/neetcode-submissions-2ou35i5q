class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        # def bfs()

        visit = set()

        area = 0

        def dfs(r , c):
            if (r<0 or c<0 or r>=rows or c>=cols or (r,c) in visit or grid[r][c]!=1):
                return 0
            visit.add((r,c))
            # return(1 + (dfs(r+1 , c) or
            #             dfs(r-1, c) or 
            #             dfs(r , c+1) or 
            #             dfs(r , c-1)))

            return (1+ (dfs(r+1 , c) +
                        dfs(r-1 , c) +
                        dfs(r ,c+1)  + 
                        dfs(r , c-1)))



        for r in range(rows):
            for c in range(cols):
                area = max(area , dfs(r ,  c))

        return area




        