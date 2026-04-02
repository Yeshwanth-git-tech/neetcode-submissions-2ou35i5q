# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:  

    def sametree(self, p , q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.sametree(p.right,q.right) and self.sametree(p.left , q.left)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #if subroot is None , it will match as there is none in root
        if not subRoot:
            return True
        #if subroot is not empty and root is empty , it will not match
        if not root:
            return False

        if self.sametree(root, subRoot):
            return True
        return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left , subRoot)