from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        if len(ransomNote) > len(magazine):
            return False
        
        
        r = Counter(ransomNote)
        m = Counter(magazine)
        
        for i in r.keys():
            if i not in m:
                return False
            if m[i] < r[i]:
                return False
        
        return True
        
        
