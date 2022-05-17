class Solution:
    def minOperations(self, nums: List[int]) -> int:
        c = 0
        for i in range(len(nums)):
            if i > 0:
                if nums[i-1]>=nums[i]:
                    diff = abs(nums[i-1]-nums[i])
                    nums[i] += diff+1
                    c+=diff+1
        return c
