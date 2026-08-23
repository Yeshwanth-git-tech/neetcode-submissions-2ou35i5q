# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        # res = 0

        def dfs(curr):
            if not curr:
                return 0

            left = dfs(curr.left)
            right = dfs(curr.right)
            #updating the max diameter , by adding left and right
            #comparing it with thememeber variable of the class res
            ##nonlocal res - so this is one more way to access the global res
            # res = max(res , left+right)
            self.res = max(self.res , left+right)
            #if we get the max value , same as max depth of the tree
            return 1 + max(left , right)

        #call the function
        dfs(root)

        return self.res