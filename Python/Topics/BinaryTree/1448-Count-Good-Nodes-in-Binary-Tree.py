# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.countGoodNodes(root, -math.inf)
    
    def countGoodNodes(self, root, ma):
        return self.countGoodNodes(root.left, max(ma, root.val)) + self.countGoodNodes(root.right, max(ma, root.val)) + (root.val >= ma) if root else 0
