# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next or not head.next.next:
            return
        
        middle = end = head

        while end.next and end.next.next:
            end = end.next.next
            middle = middle.next
        p2 = middle.next 
        middle.next = None
        prev = None
        while p2 and p2.next:
            p2next = p2.next
            p2.next = prev
            prev = p2
            p2 = p2next
        p2.next = prev

        #lets merge
        p1 = head
        while p2:
            p1next = p1.next
            p2next = p2.next
            p1.next = p2
            p2.next = p1next
            p1 = p1next
            p2 = p2next