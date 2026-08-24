# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        #so both starting at the head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        #when fast and fast.next is Null 
        return False


















        # #floyds tortoise hare

        # #we maintain a hashset
        # # hashset = defaultdict(set)
        # slow = head
        # fast = head

        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        #     if slow == fast:
        #         return True
        # return False

        # #it is linear time - O(n)

        # #that is floyds tortoise
        # #the fast pointer will catch the slow pointer in n-1 time
        # #whihc is approx O(n)


        


        