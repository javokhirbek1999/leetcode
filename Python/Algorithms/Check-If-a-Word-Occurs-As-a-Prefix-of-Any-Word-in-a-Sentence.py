class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for i in range(len(sentence.split())):
            if sentence.split()[i].startswith(searchWord):
                return i+1
        return -1
