# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # if not head:
        #     return None
        # dummy = ListNode(0 , head)
        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        second = slow.next

        # print(second.val)

        # print(slow.val)

        # slow.next = None

        # print(slow.next)

        slow.next = None
        
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            # second.next = temp
            second = temp

        second = prev
        
        # print(second.next.val)
        
        first = head

        while second:
            temp1 = first.next
            temp2 =second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
