# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    
    def serialize_rec(self, root, stream):
        
        if not root:
            stream.append(None)
            return 
        
        stream.append(root.val)
        
        self.serialize_rec(root.left, stream)
        self.serialize_rec(root.right, stream)
        
    
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        stream = []
        self.serialize_rec(root, stream)
        
        res = ""
        for i in stream:
            res+=str(i) + " "
        
        return res
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        lst = data.split(' ')
        lst.pop()
        
        root = self.deserialize_rec(lst)
        return root
        
    def deserialize_rec(self, stream):
        
        if not stream:
            return
        
        val = stream.pop(0)
 
        if val == 'None':
            return None
        
        node = TreeNode(val)
        
        node.left = self.deserialize_rec(stream)
        node.right = self.deserialize_rec(stream)
        
        return node
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
