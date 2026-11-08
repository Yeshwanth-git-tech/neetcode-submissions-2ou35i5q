class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # adj = {src:[] for src , dest in tickets}
        adj = defaultdict(list)

        for src , dest in sorted(tickets , reverse = True):
            adj[src].append(dest)
        
        res = []
        def dfs(a):
            while adj[a]:
                dfs(adj[a].pop())
            res.append(a)

        dfs("JFK")
        return res[::-1]