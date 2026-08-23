# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #nested funciton no self required
        def valid(node ,left , right):
            if not node:
                return True
            #if not is the conditon 
            if not(left<node.val and node.val< right):
                #then we can do it recursively
                return False
            
            return (valid(node.left , left , node.val)
            and valid(node.right , node.val , right))

        return valid(root , float("-inf") ,float("inf"))



        