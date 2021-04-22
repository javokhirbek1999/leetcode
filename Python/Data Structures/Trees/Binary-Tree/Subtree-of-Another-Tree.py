# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def similar(s1,t1):
            if s1 is None and t1 is None:
                return s1 == t1
            if s1 and t1:
                return s1.val == t1.val and similar(s1.left,t1.left) and similar(s1.right,t1.right)
        
        queue = [s]
        while queue:
            node = queue.pop(0)
            
            if similar(node,t):
                return True
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False
