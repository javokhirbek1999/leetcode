"""
Time: O(n)
Space: O(n)

"""
class Solution:
    def __init__(self):
        self.cache = {}
    def climbStairs(self, n: int) -> int:
        
        if n == 0:
            return 0
        
        if n == 1 or n == 2 or n == 3:
            return n
        if n-1 not in self.cache and n-2 not in self.cache:
            self.cache[n-1] = self.climbStairs(n-1)
            self.cache[n-2] = self.climbStairs(n-2)
            return self.cache[n-1]+self.cache[n-2]
        if n-1 in self.cache and n-2 not in self.cache:
            self.cache[n-2] = self.climbStairs(n-2)
            return self.cache[n-1]+self.cache[n-2]
        if n-2 in self.cache and n-1 not in self.cache:
            self.cache[n-1] = self.climbStairs(n-1)
            return self.cache[n-1]+self.cache[n-2]
        else:
            return self.cache[n-1]+self.cache[n-2]

          
