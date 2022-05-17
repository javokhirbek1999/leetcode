# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        root.val = 0
        self.vals = {}
        self.recover(root)
        self.root = root
    
    def recover(self, root) -> TreeNode:
        if not root:
            return
        self.vals[root.val] = 1
        if root.left:
            root.left.val = 2*root.val+1
        if root.right:
            root.right.val = 2*root.val+2
        
        self.recover(root.left)
        self.recover(root.right)
        

    def find(self, target: int) -> bool:
        
        return target in self.vals
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
