class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        #w , r , c

        minheap = [[grid[0][0] , 0 , 0]]

        n = len(grid)

        t = 0

        visited = set()

        directions = [[1 , 0] , [-1 , 0] , [0 , 1] , [0 , -1]]

        t = 0

        while minheap:
            w , r , c = heapq.heappop(minheap)

            if (r , c) in visited:
                continue

            visited.add((r,c))

            t = max(w , t)

            if r == n-1 and c== n-1:
                return t

            for dr , dc in directions:
                row = r+dr
                col = c+dc

                if(row<0 or col<0 or row>=n or col>=n or (row ,col) in visited):
                    continue
                heapq.heappush(minheap , [max(t , grid[row][col]) , row , col])


        
                
                
