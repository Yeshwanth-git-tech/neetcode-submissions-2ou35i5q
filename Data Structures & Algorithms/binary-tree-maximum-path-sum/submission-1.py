# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        res = [root.val]

        def dfs(root):
            if not root:
                return 0

            leftmax = dfs(root.left)
            rightmax = dfs(root.right)
            leftmax = max(leftmax , 0)
            rightmax = max(rightmax , 0)
            #with split
            res[0] = max(res[0] , root.val+leftmax+rightmax)
#             Yes, exactly. The return exists so the parent gets its leftMax or rightMax. The two values do different jobs:

# res[0]: the best path anywhere in the tree. This is the final answer.
# Return value: the best path starting at this node and going down one side. The parent needs this to build its own paths.

            return root.val+ max(leftmax, rightmax)

        dfs(root)
        return res[0]
        


        # leftMax/rightMax are clamped to 0, so this also covers
# node-only and one-sided paths