# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        if not original and not cloned:
            return True
        
        queue1 = [original]
        queue2 = [cloned]
        
        while queue1 and queue2:
            
            original_node = queue1.pop(0)
            cloned_node = queue2.pop(0)
            
            if original_node.val == target.val:
                ans = self.compare(original_node, cloned_node)
                if ans:
                    return cloned_node
            
            if original_node.left:
                queue1.append(original_node.left)
            
            if original_node.right:
                queue1.append(original_node.right)
            
            if cloned_node.left:
                queue2.append(cloned_node.left)
            
            if cloned_node.right:
                queue2.append(cloned_node.right)
        
        return None
        
    def compare(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1 and root2 or root1 and not root2:
            return False
        if root1.val != root2.val:
            return False
        
        return self.compare(root1.left, root2.left) and self.compare(root1.right,root2.right)
        
