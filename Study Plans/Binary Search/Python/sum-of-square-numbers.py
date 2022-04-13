class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        low = 0
        high = int(math.sqrt(c))
        
        while low <= high:
            
            res = low**2 + high**2
            
            if res == c:
                return True
            
            if res < c:
                low += 1
            else:
                high -= 1
        
        return False
                
            
