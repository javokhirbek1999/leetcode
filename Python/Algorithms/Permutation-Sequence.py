from itertools import permutations
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        
        t = [i for i in range(1,n+1)]
        
        temp = None
        for index, val in enumerate(permutations(t)):
            if index == k-1:
                temp = val
                break
        
        res = ""
        for i in temp:
            res+=str(i)
        
        return res
