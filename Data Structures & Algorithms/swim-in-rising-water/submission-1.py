class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N=len(grid)
        #t , r , c
        minheap = [[grid[0][0], 0 , 0]]

        visited = set()
        directions = [[0 , 1], [0 , -1] , [1,0], [-1,0]]
        visited.add((0,0))
        while minheap:
            t , r , c = heapq.heappop(minheap)
            # if (r, c) in visited:
            #     return 
            # visited.add((r,c))

            if r == N-1 and c == N-1:
                return t

            for dr , dc in directions:
                newrow = r+dr
                newcol = c+dc
                if (newrow<0 or newcol<0 or newrow == N or newcol == N or (newrow , newcol) in visited):
                    continue
                visited.add((newrow,newcol ))    
                heapq.heappush(minheap , [max(t , grid[newrow][newcol]), newrow , newcol])
                



