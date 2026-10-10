# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
    
        def countnode(node , maxval):
            if not node:
                return 0

            # res = 1 if node.val >=maxval else 0
            
            # res+=countnode(node.left , max(node.val ,maxval))
            # res+=countnode(node.right , max(node.val , maxval))

            if node.val >=maxval:
                self.res +=1

            countnode(node.left , max(node.val , maxval))
            countnode(node.right , max(node.val , maxval))


            # return res

        # return countnode(root , root.val)
        countnode(root , root.val)
        return self.res


        

            
        