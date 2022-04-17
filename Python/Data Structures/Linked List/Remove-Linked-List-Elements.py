# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        if not head:
            return head
        
        current = head
        
        while current and current.next:
            if current.next.val == val:
                while current.next and current.next.val == val:
                    current.next = current.next.next
                
            current = current.next
            
        if head and head.val == val:
                head = head.next
        return head
