class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        cache = {}
        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            # get the max total length
            max_path = 0
            for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                new_i, new_j = i + di, j + dj
                if 0 <= new_i < m and 0 <= new_j < n:
                    if matrix[new_i][new_j] > matrix[i][j]:
                        max_path = max(dfs(new_i, new_j), max_path)
                cache[(i, j)] = max_path + 1
            return max_path + 1
        
        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i, j))
        return res
