# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists and len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedlists = []
            for i in range(0 , len(lists) , 2):
                list1 = lists[i]
                list2 = lists[i+1] if (i+1) < len(lists) else None
                mergedlists.append(self.mergelist(list1 , list2))
            lists = mergedlists
        return lists[0]


    def mergelist(self, l1 , l2):
        dummy = ListNode()
        tail = dummy
        #again i forget while 
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            #forgot to update the tail pointer , wow
            tail = tail.next
        if l1:
            tail.next = l1

        if l2:
            tail.next = l2
        #forgot to return
        return dummy.next


            
        