class Solution:
    def jump(self, nums: List[int]) -> int:
        t = list(accumulate([i + num for i, num in enumerate(nums)], max))
        ind, q = 0, 0
        while ind < len(nums) - 1:
            ind = t[ind]
            q += 1
        return q
        
