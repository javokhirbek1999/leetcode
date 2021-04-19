class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        T = sum([1<<(32*n) for n in nums])
        S, ans = 1, 0
        for i in range(target):
            S = (S*T) & (1<<(32*target+32)) - 1
            ans += S >> (32*target)
            
        return ans
