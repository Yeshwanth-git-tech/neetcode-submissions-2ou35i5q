# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # if not root:
        #     return None
        q = deque([root])

        # rightside = None
        # rightside it must reset to None at the start of each level, so it goes inside the while loop.
        res = []

        while q:
            rightside = None
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    rightside = node
                    q.append(node.left)
                    q.append(node.right)


            #the right side get overwritten to rightside most node
            if rightside:
                res.append(rightside.val)

        return res

                    