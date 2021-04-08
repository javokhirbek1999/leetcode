# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
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
                    temp.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                ans.append(sum(temp)/len(temp))
            return ans    
