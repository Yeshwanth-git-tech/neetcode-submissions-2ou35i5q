class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        rank = [1]*n
        print(rank)
        par = [i for i in range(n)]
        print(par)


        def find(p):
            while p!=par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p

        
        def union(n1 , n2):
            p1 , p2 = find(n1) , find(n2)

            if p1 == p2:
                return 0
            
            if rank[p1] >= rank[p2]:
                par[p2] =p1
                rank[p1] +=rank[p2]
            else:
                par[p1] = p2
                rank[p2]+=rank[p1]

            return 1
        res = n
        for n_1, n_2 in edges:
            res-=union(n_1 , n_2)
        return res

        