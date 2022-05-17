# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        if not root:
            return ""
        
        left = '({})'.format(self.tree2str(root.left)) if (root.left or root.right) else ''
        right = '({})'.format(self.tree2str(root.right)) if root.right else ''
        return '{}{}{}'.format(root.val, left, right)
