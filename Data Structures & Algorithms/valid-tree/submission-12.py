class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        adj = {i:[] for i in range(n)}


        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visited = set()

        def dfs(node , prev):
            # if not node:
            #     return True
            if node in visited:
                return False

            visited.add(node)

            for nei in adj[node]:
                if nei == prev:
                    continue
                if not dfs(nei , node):
                    return False
            
            return True

        # return dfs(node , -1) if len(visited) == n else False
        return dfs(0 , -1) and len(visited) == n

        

        # for nodes in range(n):
        #     if not dfs(nodes , -1):
        #         return False
        # return True