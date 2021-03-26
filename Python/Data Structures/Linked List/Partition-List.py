# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Problem statement: 
# Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
# You should preserve the original relative order of the nodes in each of the two partitions.
#
# Problem Link: https://leetcode.com/problems/partition-list/

# Time: O(n) 
# Space: O(1) 
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if head is None:
            return None
                
        part1, part2 = ListNode(), ListNode()
        tail1, tail2 = part1, part2
        
        while head:
            if head.val < x:
                tail1.next = head
                tail1 = tail1.next
            else:
                tail2.next = head
                tail2 = tail2.next
            head = head.next
        
        tail1.next = part2.next
        tail2.next = None
        
        return part1.next
        
