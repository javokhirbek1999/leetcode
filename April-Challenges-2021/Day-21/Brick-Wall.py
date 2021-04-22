class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        dp = {}
        maxCount = 0
        
        for row in wall:
            idx = 0
            maxIdx = sum(row)
            for brick in row:
                idx += brick
                if idx == maxIdx:
                    continue
                count = dp.get(idx, 0) + 1
                dp[idx] = count
                if count > maxCount:
                    maxCount = count
            
        return len(wall) - maxCount
