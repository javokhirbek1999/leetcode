class TrieNode:
    
    def __init__(self, char: str) -> None:
        self.char = char
        self.children = {}
        self.count = 0
        self.end = False
        
class Trie:

    def __init__(self):
        self.root = TrieNode("")
        

    def insert(self, word: str) -> None:
        
        node = self.root
        
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                newNode = TrieNode(char)
                node.children[char] = newNode
                node = newNode
        
        node.count+=1
        node.end = True

    def search(self, word: str) -> bool:
        
        node = self.root
        
        for char in word:
            if char not in node.children:
                return False
            else:
                node = node.children[char]
        
        if node.end:
            return True
        
        return False
        

    def startsWith(self, prefix: str) -> bool:
        
        node = self.root
        
        c = 0
        
        for char in prefix:
            if char not in node.children:
                return False
            else:
                node = node.children[char]
                c+=1
        
        if node.end:
            if c == len(prefix):
                return True
            return False
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
