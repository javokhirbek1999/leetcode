class Solution:
    def minValueNode(self, node):
        current = node
        
        while current.left is not None:
            current = current.left
        
        return current
    
    
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root == None:
            return root

        
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)

        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.minValueNode(root.right)
            root.val = temp.val

            root.right = self.deleteNode(root.right, temp.val)
        
        return root
