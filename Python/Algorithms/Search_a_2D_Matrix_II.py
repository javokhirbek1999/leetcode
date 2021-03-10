class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if matrix[i].__contains__(target):
                return True
            else:
                if i == len(matrix)-1:
                    return False
