from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # adj = {i:[] for i in range(len(tickets))}
        # adj = {src:[] for src , dest in tickets}
        # adj = defaultdict(list)
        #sorted of reverse make jfk at thenend with :{}

        adj = defaultdict(list)
        # adj["KUL"]      # no KeyError → returns []
        # print(adj)      # {'KUL': []}  ← the key now exists

        # So while adj["KUL"] sees an empty list, the loop doesn't run, and KUL is appended to res
        for src , dest in sorted(tickets , reverse = True):
            adj[src].append(dest)

        print(adj)
            #Yes, adj[JFK] = [KUL, BUF]. Reverse-sorted order puts KUL before BUF , so that when we pop , it is done alphabetically


        res = []

        def dfs(src):
            while adj[src]:
                dest = adj[src].pop()
                dfs(dest)
            res.append(src)
        dfs("JFK")
        return res[::-1]
        # You may assume all the tickets form at least one valid flight path.
        #else
        # from collections import Counter

        # route = res[::-1]

        # if len(route) != len(tickets) + 1:
        #     return []

        # count = Counter(map(tuple, tickets))
        # for a, b in zip(route, route[1:]):
        #     if count[(a, b)] == 0:
        #         return []
        #     count[(a, b)] -= 1

        # return route

        



