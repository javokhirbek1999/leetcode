class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.rev(s, 0, len(s)-1)
    
    def rev(self, s: List[str], start, end):
        if start >= end:
            return s
        
        tempStart = s[start]
        tempEnd = s[end]
        s[start] = tempEnd
        s[end] = tempStart
        
        self.rev(s, start+1, end-1)
