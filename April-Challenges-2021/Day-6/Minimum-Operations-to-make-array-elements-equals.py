class Solution:
    def minOperations(self, n: int) -> int:
        mid = n//2
        return mid*(mid+n%2)
