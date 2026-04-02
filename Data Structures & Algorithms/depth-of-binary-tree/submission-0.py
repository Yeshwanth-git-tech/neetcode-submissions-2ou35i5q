# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #finding depth , #dfs
        #so we can traverse a tree bfs or dfs , for this dfs

        if not root:
            return 0

        maxx = 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        return maxx
