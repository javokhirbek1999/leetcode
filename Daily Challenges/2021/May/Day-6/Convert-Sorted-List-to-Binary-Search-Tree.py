class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def dfs(head, tail):
            if head == tail: return None
            slow = fast = head
            while fast != tail and fast.next != tail:
                slow = slow.next
                fast = fast.next.next
            return TreeNode(slow.val, dfs(head, slow), dfs(slow.next, tail))
		
        return dfs(head, None)
