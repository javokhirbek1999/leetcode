# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    
    def serializer_rec(self, root, stream):
        
        if not root:
            stream.append(None)
            return
        
        stream.append(root.val)
        
        self.serializer_rec(root.left, stream)
        self.serializer_rec(root.right, stream)

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        
        stream = []
        
        self.serializer_rec(root, stream)
        
        res = ""
        
        for i in stream:
            res += str(i) + " "
        
        return res
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        
        lst = data.split(' ')
        lst.pop()
        
        root = self.deserializer(lst)
        
        return root
    
    def deserializer(self, arr):
        
        if not arr:
            return
        
        val = arr.pop(0)
        
        if val == 'None':
            return None
        
        node = TreeNode(val)
        
        node.left = self.deserializer(arr)
        node.right = self.deserializer(arr)
        
        return node
        
# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
