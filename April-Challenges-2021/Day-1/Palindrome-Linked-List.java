
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public boolean isPalindrome(ListNode head) {
        ListNode first = head;
        ListNode second = head;
        
        while(first!=null && first.next!=null){
            first = first.next.next;
            second = second.next;
        }
        
        ListNode prev = null; 
        while(second!=null){
            ListNode temp = second.next;
            second.next = prev;
            prev = second;
            second = temp;
        }
        
        ListNode left, right;
        left = head;
        right = prev;
        while(right!=null){
            if(left.val!=right.val){
                return false;
            }
            left = left.next;
            right = right.next;
        } 
        return true;
    }
}
