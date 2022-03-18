/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func mergeKLists(lists []*ListNode) *ListNode {
    t := []int{}
    
    for _, list := range lists {
        current := list
        for current != nil {
            t = append(t, current.Val)
            current = current.Next
        }
    }
    
    sort.Slice(t, func(i, j int) bool {
        return t[i]<t[j]
    })
    
    dummy := ListNode{0, nil}
    tail := &dummy
    
    for _, val := range t {
        tail.Next = &ListNode{val, nil}
        tail = tail.Next
    }
    
    return dummy.Next
}
