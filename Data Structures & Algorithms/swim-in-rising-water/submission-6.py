class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        minheap = [[grid[0][0] , 0, 0]]
        #time t , the value [0,0]
        #r, 0
        #c, 0

        visited = set()
        directions = [[0 , 1], [0,-1], [1,0],[-1,0]]
        while minheap:
            t , r , c = heapq.heappop(minheap)

            if (r , c) in visited:
                continue
            
            visited.add((r,c))

            if r == n-1 and c== n-1:
                return t

            for dr, dc in directions:
                row = r+dr
                col = c+dc

                if (row<0 or col<0 or row == n or col ==n or (row,col) in visited):
                    continue

                heapq.heappush(minheap , [max(t,grid[row][col]), row , col])

        # return t you dont need to return t , 
        #we return when we r and c reached the bottom of the cell






