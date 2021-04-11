# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BFS: Level Order Traversal
# Runtime: Beats 94%
# Memory: Beats 71.30%
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if root is None:
            return None
        else:
            ans = []
            queue = [root]
            while queue:
                temp = []
                c = 0 
                max_len = len(queue)
                while c<max_len:
                    c+=1
                    node = queue.pop(0)
                    if node:
                        temp.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                                       
                ans.append(temp)
            return sum(ans[-1])    
                
