class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        globalMax, localMax = min(nums), min(nums)
        
        for index, value in enumerate(nums):
            if index == 0:
                localMax = value
            else:
                localMax = max(localMax+value, value)
            
            globalMax = max(globalMax, localMax)
        
        return globalMax
