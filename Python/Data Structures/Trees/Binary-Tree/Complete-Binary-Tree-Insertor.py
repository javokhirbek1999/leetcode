# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root
        self.left = None
        self.right = None

    def insert(self, v: int) -> int:
        newNode = TreeNode(v)
        if not self.root:
            self.root = newNode
            return self.root
        else:
            queue = []
            queue.append(self.root)
            while len(queue):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                else:
                    node.left = TreeNode(v)
                    return node.val
                if node.right:
                    queue.append(node.right)
                else:
                    node.right = TreeNode(v)
                    return node.val                    
            
            

    def get_root(self) -> TreeNode:
        if not self.root:
            return None
        else:
            return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()
