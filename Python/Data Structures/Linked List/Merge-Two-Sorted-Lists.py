# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None and l2 is None:
            return l1
        if l1 is None and l2:
            return l2
        if l2 is None and l1:
            return l1
             
        l = list()
        while l1 or l2:
            if l1:
                l.append(l1.val)
                l1 = l1.next
            if l2:
                l.append(l2.val)
                l2 = l2.next
                
        dummy=ListNode()
        tail = dummy
        for i in sorted(l):
            tail.next = ListNode(i)
            tail = tail.next                
        
        return dummy.next   
