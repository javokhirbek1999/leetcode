# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.diam = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.getHeight(root)
        
        return self.diam
        
    def getHeight(self, root):
        if not root:
            return 0
        
        left = self.getHeight(root.left)
        
        
        
        right = self.getHeight(root.right)
        
        self.diam = max(self.diam, left+right)
        return max(left, right)+1
