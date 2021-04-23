# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.values = []
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return None        
        self.postorderTraversal(root.left)
        self.postorderTraversal(root.right)
        if root:
            self.values.append(root.val)
        return self.values
