from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        time = 0
        rows = len(grid)
        cols = len(grid[0])

        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh+=1
                if grid[r][c] == 2:
                    q.append([r,c])

        
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        while q and fresh>0:
            #snapshot
            for i in range(len(q)):
                r , c = q.popleft()
                for dr , dc in directions:
                    row = r+dr
                    col = c+dc

                    if (row<0 or col<0 or row >=rows or col>=cols or grid[row][col]!=1):
                        continue
                    #assing it rotten as it is fresh
                    grid[row][col] = 2
                    fresh-=1
                    #dont forget to append r,c to queue
                    q.append([row,col])
            time+=1

        return time if fresh == 0 else -1




