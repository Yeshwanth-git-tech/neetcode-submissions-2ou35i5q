# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            ##this condition dont forget , so if 2
            #          1
            #         /
            #        2
            #       /
            #      3
            #     /
#             #    4
#             dfs(4): return 1
# dfs(3): left=1, right=0, diff=1 ✓, return 2
# dfs(2): left=2, right=0, diff=2 > 1 ✗ → return -1
# dfs(1): left=-1 ← comes from node 2!
# if left == -1: return -1  ← propagate up!
            if left == -1 or right ==-1:
                return -1

            if abs(left - right) > 1:
                return -1
            
            return 1 + max(left , right)

        return dfs(root) != -1