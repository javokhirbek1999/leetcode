class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        occ,acc,res=[],1,0
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                acc+=1
            else:
                occ.append(acc)
                acc=1
        occ.append(acc)
        for i in range(1,len(occ)):
            res+=min(occ[i],occ[i-1])
        return res
