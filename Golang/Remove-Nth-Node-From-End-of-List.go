/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func removeNthFromEnd(head *ListNode, n int) *ListNode {
    if head.Next == nil && n == 1 {
        head = nil
        return head
    }
    
    size := 0
    current := head
    for current != nil {
        current = current.Next
        size++
    }
    
    if n == size {
        head = head.Next
        return head
    }
    
    if n == 1 {
        current := head
        for current.Next.Next != nil {
            current = current.Next
        }
        
        current.Next = nil
        return head
        
    }
    slow, fast := head, head
    
    for i := 0; i<n; i++ {
        fast = fast.Next
    }
    
    for fast.Next != nil {
        slow = slow.Next
        fast = fast.Next
    }
    
    slow.Next = slow.Next.Next
    
    return head
}
