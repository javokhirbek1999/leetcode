# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head is None:
            return None
        
        if head.next is None:
            head = None
            return head
        
        current = head
        c = 0
        
        while current:
            current = current.next
            c += 1
        if c == n:
            head = head.next
            return head
        
        t = 0
        current = head
        while current:
            if t==(c-n-1):
                current.next = current.next.next
            current = current.next
            t+=1
        return head
                
