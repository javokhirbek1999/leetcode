class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        arr = [[s.count('0'), s.count('1')] for s in strs]
        
        @lru_cache(None)
        def dp(i, m, n):
            if i == len(strs):
                return 0
            
            ans = dp(i+1, m, n) # Skip strs[i]
            if m >= arr[i][0] and n >= arr[i][1]:
                ans = max(ans, dp(i+1, m-arr[i][0], n-arr[i][1]) + 1) # Pick strs[i]
            return ans
        
        return dp(0, m, n)
