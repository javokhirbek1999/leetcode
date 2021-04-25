class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        r = []
        for i in range(len(matrix)):
            t = []
            for j in range(len(matrix[i])):
                t.append(matrix[j][i])
            r.append(t)
        matrix.clear()
        matrix.extend(r)
        
