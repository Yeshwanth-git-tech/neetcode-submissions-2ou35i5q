# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

        #you frgot to update the pointer inside while loop for tail
            tail = tail.next

            #if one of the list gets empty after comparing all the values and merged we just append the remaining linkedlist to tail
        #dont forget to exit the while loop
        if list1:
            tail.next = list1
        else:
            tail.next = list2

        return dummy.next
        #as tail is the head
            