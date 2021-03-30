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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        if (head == null){
            return null;
        }
        
        if (head.next == null){
            head = null;
            return head;      
        }        
        
        ListNode current = head;
        int c = 0;             
                
        while (current!=null){
            current = current.next;
            c += 1;
        }        
        if (c == n){
            head = head.next;
            return head;
        }    
                
        
        int t = 0;
        current = head;         
        while (current!=null){
            if (t==(c-n-1)){
                current.next = current.next.next;
            }
            current = current.next;
            t+=1;
        }
        return head;    
    }
}
