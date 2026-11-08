class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        q = deque()
        visited = set()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]== 2:
                    q.append((r , c))
                    visited.add((r,c))
                if grid[r][c]== 1:
                    fresh+=1


        time = 0
        directions = [[1 , 0] , [-1 ,0] , [0 , 1] , [0 , -1]]
        while q and fresh > 0:
            for i in range(len(q)):
                r , c = q.popleft()
                # grid[r][c] = dist

                for dr , dc in directions:
                    row = r + dr
                    col = c + dc

                    if (row<0 or col<0 or row == rows or col == cols or (row , col) in visited or grid[row][col]!=1):
                        continue
                    q.append((row,col))
                    visited.add((row,col))
                    fresh-=1
            time+=1
        
        return time if fresh ==0 else -1
                    
        