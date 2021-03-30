class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        c = 0
        for i in range(1,n+1):
            if n%i==0:
                if c+1==k:
                    return i
                c+=1
        return -1
 
# Problem statement:
#   Given two positive integers n and k.
#   A factor of an integer n is defined as an integer i where n % i == 0.
#   Consider a list of all factors of n sorted in ascending order, return the kth factor in this list or return -1 if n has less than k factors.
# 
# Link: https://leetcode.com/problems/the-kth-factor-of-n/      
