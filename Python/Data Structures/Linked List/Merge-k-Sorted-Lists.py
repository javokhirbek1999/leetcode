# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nums = []
        
        for i in lists:
            current = i
            while current:
                nums.append(current.val)
                current = current.next
        
        nums.sort()
        
        dummy = ListNode(0)
        tail = dummy
        
        for i in nums:
            tail.next = ListNode(i)
            tail = tail.next
        
        return dummy.next
