# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> List:
        if head is None:
            return head
        t = []
        b = head
        while b:
            t.append(b.val)
            b = b.next
        
        t.sort()
        tail = head
        for i in t:
            tail.next = ListNode(i)
            tail = tail.next
        return head.next    
