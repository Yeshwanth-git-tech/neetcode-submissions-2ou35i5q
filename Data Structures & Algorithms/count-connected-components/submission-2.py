class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjmap = {i:[] for i in range(n)}

        for n1 , n2 in edges:
            adjmap[n1].append(n2)
            adjmap[n2].append(n1)

        visited = set()
        def dfs(node):
            if node in visited:
                return

            visited.add(node)

            for nei in adjmap[node]:
                dfs(nei)

        
        count = 0 

        for i in range(n):
            if i not in visited:
                dfs(i)
        # count+=1
        #so after the call is completed , 
        #we ahave to add the count whcih all thenmodes conencted are added to visited set
                count+=1

        return count