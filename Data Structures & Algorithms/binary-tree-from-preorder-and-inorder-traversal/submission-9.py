# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # in preorder , the root comes first

        #base case 
        # if not preorder or not inorder:
        #     return None

        # root = TreeNode(preorder[0])
        # mid = inorder.index(preorder[0])
        # #we exclude 0 as that is the root
        # #1 , 2 , 3  , 4
        # #1 is the root , index of 1 in preorder is mid , now left is 2 in inorder and in preorder that mid+1

        # # left = self.buildTree(preorder[1:mid+1] , inorder[:mid])
        # # right = self.buildTree(preorder[mid+1:] , inorder[mid+1:])
        # # you frget to add root.left , root.right
        # root.left = self.buildTree(preorder[1:mid+1] , inorder[:mid])
        # root.right = self.buildTree(preorder[mid+1:] , inorder[mid+1:])
        
        # return root

        pos = {v: i for i, v in enumerate(inorder)}
        self.pre = 0

        def build(l, r):
            if l > r:
                return None
            val = preorder[self.pre]
            self.pre += 1
            root = TreeNode(val)
            mid = pos[val]
            root.left = build(l, mid - 1)
            root.right = build(mid + 1, r)
            return root

        return build(0, len(inorder) - 1)
        