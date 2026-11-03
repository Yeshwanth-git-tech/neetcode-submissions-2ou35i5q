class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        fresh = 0
        q = deque()
        visited = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh+=1
                if grid[r][c] == 2:
                    q.append([r, c])
                    visited.add((r,c))


        directions =[[1 , 0] , [-1 , 0] , [0 , 1] , [0 ,-1]]
        t = 0
        # while q:
        #stop one nothjing fresh is left
        while q and fresh > 0:
            for i in range(len(q)):
                r , c = q.popleft()

                for dr , dc in directions:
                    row = r + dr
                    col = c + dc

                    if (row <0 or col <0 or row >= rows or col>=cols or (row , col) in visited 
                        or grid[row][col] !=1):
                        continue
                    grid[row][col] = 2
                    visited.add((row , col))
                    q.append([row , col])
                    fresh-=1

            t+=1
        return t if not fresh else -1
