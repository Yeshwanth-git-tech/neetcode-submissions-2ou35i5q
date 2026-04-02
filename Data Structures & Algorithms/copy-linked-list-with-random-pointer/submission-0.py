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
        if not head: return None
        
        oldtocopy = {}
        curr = head

        while curr:
            node = Node(x = curr.val)
            oldtocopy[curr] = node
            curr = curr.next
        

        curr = head
        while curr:
            #copying
            new_node = oldtocopy[curr]
            new_node.next = oldtocopy[curr.next] if curr.next else None
            new_node.random = oldtocopy[curr.random] if curr.random else None
            #we will move the pointer
            curr = curr.next

        return oldtocopy[head]

