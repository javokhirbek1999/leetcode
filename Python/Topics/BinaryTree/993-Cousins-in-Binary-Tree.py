# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root:
            return True
        
        queue = [root]
        
        while queue:
            
            x_n, y_n = False, False
            n = len(queue)
            
            while n > 0:
                
                node = queue.pop(0)
                
                if node.val == x:
                    x_n = True
                if node.val == y:
                    y_n = True
                
                if node.left and node.right:
                    if node.left.val == x and node.right.val == y or node.left.val == y and node.right.val == x:
                        return False
                
                n-=1
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            
            if x_n and y_n:
                return True
            
