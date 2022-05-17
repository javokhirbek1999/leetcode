# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1
        
        queue = [root]
        
        vals = []
        
        while queue:
            
            node = queue.pop(0)
            
            vals.append(node.val)
            
            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)
        
        vals.sort()
        mn = abs(vals[0]-vals[1])
        
        for i in range(1,len(vals)-1):
            mn = min(mn, abs(vals[i]-vals[i+1]))
        
        return mn
        
