class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])

        q = deque()
        visited = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]== 0:
                    q.append((r , c))
                    visited.add((r,c))
        dist = 0
        directions = [[1 , 0] , [-1 ,0] , [0 , 1] , [0 , -1]]
        
        while q:
            for i in range(len(q)):
                r , c = q.popleft()
                grid[r][c] = dist

                for dr , dc in directions:
                    row = r + dr
                    col = c + dc

                    if (row<0 or col<0 or row == rows or col == cols or (row , col) in visited or grid[row][col]==-1):
                        continue
                    q.append((row,col))
                    visited.add((row,col))
            dist+=1
            
        