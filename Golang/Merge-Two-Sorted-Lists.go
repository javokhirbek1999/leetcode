/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
// import (
    // "sort"
    // "fmt"
// )
func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
    
    current := list1
    vals := []int{}
    
    for current != nil {
        vals = append(vals, current.Val)
        current = current.Next
    }
    
    current = list2
    
    for current != nil {
        vals = append(vals, current.Val)
        current = current.Next
    }
    
    sort.Slice(vals, func(i, j int) bool {
        return vals[i]<vals[j]
    })
    
    dummy := ListNode{0, nil}
    tail := &dummy
    
    for _, val := range vals {
        tail.Next = &ListNode{val, nil}
        tail = tail.Next
    }

    return dummy.Next
}
