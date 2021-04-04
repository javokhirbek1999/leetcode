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
        ans = []
        queue = deque()
        queue.append(root)
        while queue:
            temp = []
            cnt = 0
            max_size = len(queue)
            while cnt < max_size:
                cnt+=1
                node = queue.popleft()
                temp.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            ans.append(temp)
        return ans    
    
            
        

