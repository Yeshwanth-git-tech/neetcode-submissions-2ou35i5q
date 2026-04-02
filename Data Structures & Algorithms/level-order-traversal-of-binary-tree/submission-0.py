# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res= []

        q = collections.deque()
        q.append(root)

        while q:
            #until the q exists
            lenq = len(q)
            #empty list to add node values of each level
            level = []
            #loop tthrough every node of single level
            for i in range(lenq):
                #first in first out
                node = q.popleft()
                #if the queue is not empty
                if node:
                    #we will add the value to the level
                    level.append(node.val)
                    #add the children of the node to queue
                    q.append(node.left)
                    q.append(node.right)

            if level:
                res.append(level)

        return res
