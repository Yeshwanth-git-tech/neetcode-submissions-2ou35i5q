# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:


        if not root:
            return 

        stack = [root]

        n = 0

        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            print(curr)
            curr = stack.pop()
            n+=1
            if n == k:
                return curr.val
            curr = curr.right
            
        # while curr:
        #         curr = curr.left
        #     stack.append(curr)

            

        #     if k > 0:
        #         curr = stack.pop()
        #         k-=1
                
        #     curr = curr.right