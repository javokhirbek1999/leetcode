"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:    
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        stack = [root]
        popped = []
        while stack:
            node = stack.pop()
            popped.append(node.val)
            for i in node.children[::-1]:
                stack += [i]
        return popped
