# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:    
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = []
        ans = []
        queue.append(root)
        while queue:
            temp = []
            cnt = 0
            max_len = len(queue)
            while cnt<max_len:
                cnt+=1
                node = queue.pop(0)
                temp.append(node.val)
                if(node.left):
                    queue.append(node.left)
                if(node.right):
                    queue.append(node.right)
            ans.append(temp)        
        return ans    
    
            
        

