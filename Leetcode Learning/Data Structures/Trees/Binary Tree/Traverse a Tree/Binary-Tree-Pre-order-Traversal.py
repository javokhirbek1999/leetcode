# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.values = []
    def preorderTraversal(self, root: TreeNode) -> List[int]:        
        if not root:
            return self.values
        if root:
            self.values.append(root.val)
        self.preorderTraversal(root.left)    
        self.preorderTraversal(root.right)    
        return self.values        
