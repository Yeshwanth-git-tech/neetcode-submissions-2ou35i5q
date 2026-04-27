# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #recursive dfs
        # if not root:
        #     return 0

        # return 1+ max(self.maxDepth(root.left) , self.maxDepth(root.right))

        #iterative dfs

        # stack = []
        # stack.append([root , 1])
        # res = 0
        
        # while stack:
        #     node , depth = stack.pop()
        #     if node:
        #         res = max(res ,depth)
        #         stack.append([node.left , depth+1])
        #         stack.append([node.right , depth+1])
        # return res

        #bfs
        if not root:
            return 0

        q = deque([root])
        # q.append(root)
        level = 0
        while q:
            qlen=len(q)
            for _ in range(qlen):
                node = q.popleft()
                # if node:
                #we have to check both the nodes
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            level+=1
                    
        return level



