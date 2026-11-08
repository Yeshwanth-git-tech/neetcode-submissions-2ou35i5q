class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        heap = [[grid[0][0] , 0 , 0]]
        #the value , r , c 

        visited = set()

        n = len(grid)
        
        directions = [[1 , 0] , [-1 , 0], [0 , 1] , [0 , -1]]

        t = 0
            
        while heap:
            w , r, c = heapq.heappop(heap)

            if (r,c) in visited:
                continue

            #again i forgot , but i found it mudelgf
            visited.add((r, c))
            
            t = max(t , w)
         
            if r == (n-1) and c ==(n-1):
                return t
            
            for dr ,dc in directions:
                row = r+dr
                col = c+dc

                if (row<0 or col<0 or row >=n or col>=n or (row ,col) in visited):
                    continue
                heapq.heappush(heap , [max(grid[row][col] , t) , row , col])

        # return t
            