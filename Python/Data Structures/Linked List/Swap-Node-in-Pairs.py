# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next is None or head is None:
            return head
        h = ListNode(head.next.val)
        self.swap(head)
        h.next = head
        return h
        
    
    def swap(self, head):
        if not head or not head.next:
            return head
        p1 = head
        p2 = head.next
        p3 = p2.next
        
        p1.next = p3
        p2.next = p1
        
        if p3:
            p1.next = self.swap(p3)
        return p2
        
