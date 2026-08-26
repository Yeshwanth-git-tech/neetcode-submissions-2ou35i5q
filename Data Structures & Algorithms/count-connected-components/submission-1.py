class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj = {i:[]for i in range(n)}

        #i am createing a hashmap with values as list of neughbours of the nodes

        #now lets append the edges


        for n1 , n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        #now i need a set to avoid looping 

        visit = set()

        #dfs

        def dfs(node):
            if node in visit:
                return 

            visit.add(node)

            for neighbour in adj[node]:
                dfs(neighbour)

        #so this will loop through the adj hashmap with value list to add to visit set
        components = 0
        for i in range(n):
            #so basically if the edge is not there in hashset
            if i not in visit:
                #lets dfs
                dfs(i)
                components+=1

        return components


