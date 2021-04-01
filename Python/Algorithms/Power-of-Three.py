class Solution:
    def isPowerOfThree(self, n: int) -> bool:        
        t = 1
        if n == 1:
            return True
        while True:
            t=t*3
            if t==n:
                return True
            elif t>n:
                 return False   
