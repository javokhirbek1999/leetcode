class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        t = int(math.floor(math.sqrt(num)))
        
        if t*t == num:
            return True
        return False
