class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)+1
        par = [i for i in range(n)]
        rank = [1]*n

        def find(n1):
            while n1!=par[n1]:
                par[n1] = par[par[n1]]
                n1 = par[n1]
            return n1

        def union(n1 , n2):
            p1 , p2 = find(n1) , find(n2)

            if p1 == p2:
                # return [n1 , n2]
                return False
            
            if rank[p1] >= rank[p2]:
                par[p1] = p2
                rank[p1]+=rank[p2]
            else:
                par[p2] = p1
                rank[p2]+=rank[p1]
            return True
        
        for e1 , e2 in edges:
            if not union(e1 , e2):
                return [e1 , e2]
        

        