# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(node ,maxval):
            if not node:
                return 0

            if node.val >=maxval:
                self.res+=1

            # left = dfs(node.left , max(node , node.val))
            # right = dfs(node.right , max(node , node.val))

            left = dfs(node.left , max(node.val , maxval))
            right = dfs(node.right , max(node.val, maxval))

        dfs(root , root.val)
        return self.res




        

            
        