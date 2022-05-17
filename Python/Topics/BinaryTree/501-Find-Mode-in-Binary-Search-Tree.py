# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        vals = {}
        queue = [root]
        
        while queue:
            
            node = queue.pop(0)
            
            if node.val in vals:
                vals[node.val]+=1
            else:
                vals[node.val] = 1
            
            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)
        
        vals = dict(sorted(vals.items(), key=lambda x:x[1]))
        
        mx = list(vals.values())[-1]
        
        return [i for i in vals.keys() if vals[i] == mx]
        
