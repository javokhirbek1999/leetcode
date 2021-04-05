class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        maximum = 0
        for i in range(len(A)-2):
            maximum = max(maximum,A[i])
            if(maximum>A[i+2]):
                return False
        return True
