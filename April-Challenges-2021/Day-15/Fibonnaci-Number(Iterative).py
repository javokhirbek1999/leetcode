class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n==1:
            return 1
        i = 0
        next_t = 1
        prev_t = 0
        p_t = 1
        while i < n:
            next_t = prev_t+p_t
            p_t = prev_t
            prev_t = next_t
            i+=1
        return next_t    
         
            
