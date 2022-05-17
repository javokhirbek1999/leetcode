# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        self.remove(root, target)
        if root and not root.left and not root.right and root.val == target:
            root = None
        return root
    
    def remove(self, root, val):
        if not root:
            return 
        self.remove(root.left, val)
        self.remove(root.right, val)
        if root.left:
            if root.left.val == val and not root.left.left and not root.left.right:
                root.left = None
        if root.right:
            if root.right.val == val and not root.right.left and not root.right.right:
                root.right = None
        
