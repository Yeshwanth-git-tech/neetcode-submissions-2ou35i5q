# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #pre order traversal 

        res = []

        def countgoodnodes(node , maxval):
            # so root node is always good node
            if not node:
                return 0
            
            res = 1 if node.val >= maxval else 0
            maxval = max(maxval ,node.val)
            res+= countgoodnodes(node.left , maxval)
            res+= countgoodnodes(node.right , maxval)

            return res

        return countgoodnodes(root , root.val)

            