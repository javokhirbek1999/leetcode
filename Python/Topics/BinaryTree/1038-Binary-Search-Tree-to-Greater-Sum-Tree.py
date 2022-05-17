# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sum = 0
        
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.trav(root)
        return root
    
    def trav(self, root):
        if not root:
            return
        self.trav(root.right)
        self.sum+=root.val
        root.val = self.sum
        self.trav(root.left)
        
