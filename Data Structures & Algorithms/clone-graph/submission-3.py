"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldtocopy = {}

        def dfs(root):
            if root in oldtocopy:
                return oldtocopy[root]

            copy = Node(root.val)
            oldtocopy[root] = copy

            # for nei in oldtocopy[root]:
            #     copy.neighbors.append(dfs(nei))

            for nei in root.neighbors:
                 copy.neighbors.append(dfs(nei))

            # return oldtocopy[copy]
            return copy
        
        return dfs(node) if node else None
        