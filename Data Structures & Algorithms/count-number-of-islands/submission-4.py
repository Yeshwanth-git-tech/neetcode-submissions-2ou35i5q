class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        visited = set()


        def dfs(r , c):
            if (r<0 or c<0 or r>=rows or c>= cols or(r,c) in visited or grid[r][c]!="1"):
                return
                # return False

            visited.add((r,c))

            # res = (dfs(r+1, c) or dfs(r-1 , c) or dfs(r, c+1) or dfs(r , c-1))
            dfs(r+1, c) 
            dfs(r-1 , c)  
            dfs(r, c+1) 
            dfs(r , c-1)

            # return True


        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    # if dfs(r , c):
                    dfs(r , c)
                    res+=1

        return res