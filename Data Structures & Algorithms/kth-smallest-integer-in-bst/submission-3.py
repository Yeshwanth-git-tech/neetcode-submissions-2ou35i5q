# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        n = 0

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            n+=1
            if n == k:
                return curr.val

            curr = curr.right

    #so here we add it i in poost order and then while we pop it is inorder so it is awesome

    #4 , 3 , 2, - we pop , 2 n = 1, 3 n=2, 4 n = 3,curr = curr.right  5 , n=4 , so we r then we return 5


        
            
        