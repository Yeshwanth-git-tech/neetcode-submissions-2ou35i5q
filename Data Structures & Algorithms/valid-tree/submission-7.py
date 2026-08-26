class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        # #base condiotn 
        # if not n:
        #     return True #empty graph is avalid tree
        # adj = {i:[] for i in range(n)}

        # for n1 , n2 in edges:
        #     adj[n1].append(n2)
        #     #since it is unidrected
        #     adj[n2].append(n1)

        # visit = set()

        # def dfs(i , prev):
        #     if i in visit:
        #         return False
        #     #you ahve to add to visit here
        #     visit.add(i)
        #     for j in adj[i]:
        #         if j == prev:
        #             continue
        #             #to avoid false positive
        #         if not dfs(j , i): return False
        #     #now all conditons are passed , now there is no loop
        #     return True
        #         # visit.add(j)

        # #call the funciton
        # #Here we start from 0 as all the edhge will always start from zero
        # #and keep the previous -1 as there cant be a node with neagative value
        # #as the values start from 0
        # #so that no node is unconnected and we have to check the node is th etreee 
        # #we have traversed == the total number of edge
        # return dfs(0 , -1) and n == len(visit)
        # #0 through n-1 provided in the qn

        #even if the if there is only edge then too it is valid 

        if not n:
            return True

        adj = {i:[] for i in range(n)}

        for n1 , n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visit = set()

        def dfs(i , prev):
            if i in visit:
                return False

            # if adj[i] == []:
            #     return True

            visit.add(i)

            # print(visit)

            for j in adj[i]:
                if j == prev:
                    continue
                #if this is not true , then return False
                # if not dfs(j , prev)
                #now i is prev
                if not dfs(j , i): return False
            #all the conditons are passed
            return True

        #graph starts at 0 and prev = -1 and only if all the nodes are visited , that is all the edges
        return dfs(0 , -1) and n == len(visit)

        