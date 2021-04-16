class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        c,i = 1,1
        while i < len(s):
            if s[i]==s[i-1]:
                c+=1
            else:
                c=1
            if c == k:
                s = self.removeDuplicates(s[:i-k+1]+s[i+1:],k)
            i+=1
        return s    
        
