# Problem statement:
# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        t = 0
        dummy = ListNode()
        tail = dummy
        
        while l1 or l2:
            result = t
            if l1:
                result += l1.val
                l1 = l1.next 
            if l2:
                result += l2.val
                l2 = l2.next
            tail.next = ListNode(result%10) 
            t = result//10
            tail = tail.next
            
        if t>0:    
            tail.next = ListNode(t)    
            
        return dummy.next 
      
# Problem Link: https://leetcode.com/problems/sum-of-two-integers/      
