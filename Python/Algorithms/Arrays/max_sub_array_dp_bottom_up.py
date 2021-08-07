class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        sub_sols = [None] * len(nums)
        
        for i in range(len(nums)):
            if i == 0:
                sub_sols[i] = nums[0]
            else:
                sub_sols[i] = max(nums[i], sub_sols[i-1]+nums[i])
        
        max_val = min(nums)
        
        for j in range(len(nums)):
            max_val = max(max_val, sub_sols[j])
        return max_val
    
        
