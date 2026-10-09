class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        par = [i for i in range(n)]
        rank = [1]*n


        def find(p):
            while p!=par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p

        def union(n1, n2):
            p1 , p2 = find(n1), find(n2)

            if p1 == p2:
                return 0

            if rank[p1]>=rank[p2]:
                par[p2] = p1
                rank[p1]+=rank[p2]
            else:
                par[p1] = p2
                rank[p2]+=rank[p1]
            return 1

        res = n
        for n1 , n2 in edges:
            res-=union(n1 , n2)

        return res



        # adjmap = {i:[] for i in range(n)}

        # for n1 , n2 in edges:
        #     adjmap[n1].append(n2)
        #     adjmap[n2].append(n1)

        # visited = set()
        # def dfs(node):
        #     if node in visited:
        #         return

        #     visited.add(node)

        #     for nei in adjmap[node]:
        #         dfs(nei)

        
        # count = 0 

        # for i in range(n):
        #     if i not in visited:
        #         dfs(i)
        # # count+=1
        # #so after the call is completed , 
        # #we ahave to add the count whcih all thenmodes conencted are added to visited set
        #         count+=1

        # return count