"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldtocopy = {None: None}

        curr = head
        while curr:
            #node(3)
            copy = Node(curr.val)
            #this will store the node 3 with copy value -{3:copyvalue}
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

