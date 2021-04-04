# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node:
                node.left,node.right = node.right,node.left
                queue.append(node.left)
                queue.append(node.right)
        return root        
