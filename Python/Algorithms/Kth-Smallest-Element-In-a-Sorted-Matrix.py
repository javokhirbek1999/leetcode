class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        t = []
        for i in matrix:
            for j in i:
                t.append(j)
        t.sort()
        return t[k-1]
