
class WordFilter:

    def __init__(self, words: List[str]):
        self.words = {}
        for index,word in enumerate(words):
            rev = word[::-1] # Reverse each word
            for i in range(len(word)+1):
                for j in range(len(word)+1):
                    self.words[(word[:i],rev[:j])] = index
        
    def f(self, prefix: str, suffix: str) -> int:
        suffix = suffix[::-1] # Reverse the suffix
        if (prefix,suffix) not in self.words:
            return -1
        return self.words[(prefix,suffix)]


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
