"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


# Key: the original node
# Value: its copy node
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldtocopy = {None:None}

        curr = head
        while curr:
            copy = Node(curr.val)
            oldtocopy[curr] = copy
            curr = curr.next
        #reassign the curr
        curr = head
        while curr:
            copy = oldtocopy[curr]
            copy.next = oldtocopy[curr.next]
            copy.random = oldtocopy[curr.random]
            curr = curr.next

        return oldtocopy[head]



        