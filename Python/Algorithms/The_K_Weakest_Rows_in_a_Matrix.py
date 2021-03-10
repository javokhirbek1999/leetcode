class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        sorted_version = sorted(mat)
        indices = []
        for i in range(len(mat)):
            index = mat.index(sorted_version[i])
            indices.append(index)
            mat[index] = [None]
        return indices[:k]
        
