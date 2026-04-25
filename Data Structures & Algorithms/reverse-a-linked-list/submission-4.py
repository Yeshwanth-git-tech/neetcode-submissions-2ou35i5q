# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # prev = None
        # curr = head
        # while curr:
        #     tmp = curr.next
        #     curr.next = prev
            
        #     prev  = curr
        #     # curr = prev.next
        #     curr = tmp
        # return prev

        ##recursive
        if not head or not head.next:
            return head

        newhead = self.reverseList(head.next)
        #so this will stop at 3 and start to rewind

        head.next.next = head
        head.next = None

        return newhead

