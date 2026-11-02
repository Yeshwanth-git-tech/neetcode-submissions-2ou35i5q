# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #so for this the node must be greater than prev max value int he path
    
        self.res = 0
        def dfs(node , maxval):
            if not node:
                return 0
            
            if node.val >= maxval:
                self.res+=1
            #we want to avoid negative values
            # dfs(node.left , max(node.left.val , node.val))
            # dfs(node.right , max(node.right.val , node.val))
            dfs(node.left , max(node.val , maxval))
            dfs(node.right , max(node.val , maxval))

    
        dfs(root, root.val)
        return self.res