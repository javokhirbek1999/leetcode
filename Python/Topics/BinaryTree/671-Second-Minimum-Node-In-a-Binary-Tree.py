# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1
        
        vals = {}
        
        queue = [root]
        
        while queue:
            
            node = queue.pop(0)
            
            vals[node.val] = 1
            
            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)
        
        if len(vals) == 1:
            return -1
        return sorted(vals.keys())[1]
        
