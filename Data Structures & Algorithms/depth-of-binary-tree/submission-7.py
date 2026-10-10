# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        ##dfs
        # if not root:
        #     return 0

        # return 1 + max(self.maxDepth(root.left) , self.maxDepth(root.right))
        ##bfs
        # if not root:
        #     return 0

        # q = deque([root])

        # depth = 0

        # while q:
        #     for _ in range(len(q)):
        #         node = q.popleft()
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #     depth+=1

        # return depth

        stack = [[root , 1]]

        res = 0
        #even if root is none , then after pop we will check if node , this will give us false
        #so res willl be 0
        while stack:
            node , d = stack.pop()
            if node:
                res = max(d , res)
                stack.append([node.left , d+1])
                stack.append([node.right , d+1])

        return res



        
        