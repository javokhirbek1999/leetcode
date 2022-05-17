# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        
        def buildTree(r, val):
            if not r:
                r = TreeNode(val)
                return
            else:
                if val < r.val:
                    if not r.left:
                        r.left = TreeNode(val)
                        return
                    else:
                        buildTree(r.left, val)
                else:
                    if not r.right:
                        r.right = TreeNode(val)
                        return
                    else:
                        buildTree(r.right, val)
        
        for i in preorder[1:]:
            buildTree(root, i)
        
        return root
                        
