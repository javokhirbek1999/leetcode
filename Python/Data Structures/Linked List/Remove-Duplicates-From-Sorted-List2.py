# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Problem Statement:
#
# Given the head of a sorted linked list, delete all nodes that have duplicate numbers, 
# leaving only distinct numbers from the original list. Return the linked list sorted as well.
#
# Input: head = [1,2,3,3,4,4,5]
# Output: [1,2,5]
#
# Problem Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        current = head
        duplicates = set([])
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
                duplicates.add(current.val)
            else:
                current = current.next
        
        node = ListNode()
        node.next = head
        current = node
        while current and current.next:
            if current.next.val in duplicates:
                current.next = current.next.next
            else:
                current = current.next
            
        return node.next   
      
