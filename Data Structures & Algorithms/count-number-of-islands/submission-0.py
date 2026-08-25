from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #i will use bfs , queue datastructre for it
        #hashset to avoid countig the nighbour as seperate island

        visit = set()
        islands = 0

        rows = len(grid)
        cols = len(grid[0])

        def bfs(r,c):
            q = []
            #adding this island r, c as a tuple
            q.append((r,c))
            visit.add((r,c))

            while q:
                #if dfs just pop  last added element thats only the difference and q = []
                row,col = q.pop()
                directions = [(-1, 0),(1 ,0),(0 , 1),(0,-1)]
                for dr , dc in directions:
                    r = row + dr
                    c = col + dc

                    if r in range(rows) and c in range(cols) and (r,c) not in visit and grid[r][c] == "1":
                        visit.add((r,c))
                        q.append((r,c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands+=1

        return islands




        