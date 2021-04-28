class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)-1
        n = len(obstacleGrid[0]) - 1
        dp = [[0 for j in range(n+1)] for i in range(m+1)]
        dp[0][0] = 1-obstacleGrid[0][0]
        for i in range(1,m+1):
            if obstacleGrid[i][0]!=1:
                dp[i][0] = dp[i-1][0]
        for j in range(1,n+1):
            if obstacleGrid[0][j]!=1:
                dp[0][j] = dp[0][j-1]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if obstacleGrid[i][j]!=1:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m][n]
