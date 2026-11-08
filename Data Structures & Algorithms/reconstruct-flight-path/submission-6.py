class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()

        adj = defaultdict(list)
        for src, dst in sorted(tickets, reverse=True):
            adj[src].append(dst)
        
        res = []

        def dfs(a):
            while adj[a]:
                dfs(adj[a].pop())
            res.append(a)

        dfs("JFK")
        return res[::-1]