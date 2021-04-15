class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if head is None:
            return None
        
        p1,p2 = ListNode(),ListNode()
        t1,t2 = p1,p2
        
        while head:
            if head.val < x:
                t1.next = head
                t1 = t1.next
            else:
                t2.next = head
                t2 = t2.next
            head = head.next
        
        t1.next = p2.next
        t2.next = None
        
        return p1.next
