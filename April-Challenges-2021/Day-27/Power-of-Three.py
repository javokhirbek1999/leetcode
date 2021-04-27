class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        return pow(3,int(math.log(abs(n))))==n or pow(3,int(math.log(abs(n))))//3==n
            
