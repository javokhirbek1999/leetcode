class Solution:
    def fib(self, n: int) -> int:
        if n < 1:
            return n
        else:    
            total = self.fib(n-1)+self.fib(n-2)
            return abs(total)
