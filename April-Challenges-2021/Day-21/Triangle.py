class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = {}
        def ans(n,idx,last):
            if (n,idx) in dp:
                return dp[(n,idx)]
            if n >= len(triangle):
                dp[(n,idx)] = last
                return last
            dp[(n,idx)] = last+min(ans(n+1,idx,triangle[n][idx]),ans(n+1,idx+1,triangle[n][idx+1]))
            return dp[(n,idx)]
        return ans(1,0,triangle[0][0])
