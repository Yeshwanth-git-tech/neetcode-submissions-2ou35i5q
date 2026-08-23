# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 
    #helper function
    def issametree(self , p , q):
        if not p and not q:
            return True 

        if not p or not q:
            return False

        if p.val!= q.val:
            return False
        
        return (self.issametree(p.left , q.left) and self.issametree(p.right , q.right))

        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #base conditions
        #the subtree can be empty and tree cannot be empty
        if not subRoot:
            return True
        if not root:
            return False

        if self.issametree(root ,subRoot):
            return True

        #  return (self.isSubtree(root.left , subRoot.right) and self.isSubtree(root.right , root.left))
        # return (self.isSubtree(root.left , subRoot.right) 
        # or self.isSubtree(root.right , root.left))
        ##you are checking with the subroot with the root.left and root.right
        return (self.isSubtree(root.left , subRoot)
        or self.isSubtree(root.right , subRoot))
        
       