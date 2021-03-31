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
    public ListNode sortList(ListNode head) {
        if(head==null) {
            return null;
        }
        
        ArrayList<Integer> list = new ArrayList<>();
        ListNode b = head;
        
        while(b!=null){
            list.add(b.val);
            b = b.next;
        }
        
        Collections.sort(list);
        ListNode tail = head;
        for(Integer i:list){
            tail.next = new ListNode(i);
            tail = tail.next;
        }
        return head.next;
            
    }
}
