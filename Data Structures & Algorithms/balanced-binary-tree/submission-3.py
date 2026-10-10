# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.diff = 0
        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)

            right = dfs(node.right)

            self.diff = max(self.diff , abs(left - right))
            if self.diff > 1:
                return False
            return 1 + max(left , right)


        dfs(root) 
        return True if not self.diff > 1 else False
        