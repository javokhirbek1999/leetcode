# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.items = []
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return self.items
        self.inorderTraversal(root.left)
        if root:
            self.items.append(root.val)
        self.inorderTraversal(root.right)
        return self.items
            
