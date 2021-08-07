class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        sub_sols = [None] * len(nums)
        
        if len(nums) == 1:
            return nums[0]
        
        def max_sub_array_ending_at(i):
            if i == 0:
                return nums[0]
            if sub_sols[i]:
                return sub_sols[i]
            m = max(nums[i],max_sub_array_ending_at(i-1)+nums[i])
            sub_sols[i] = m
            return m
        
        max_value = min(nums)
        
        for j in range(len(nums)):
            max_value = max(max_value, max_sub_array_ending_at(j))
        
        return max_value
        
            
    
        
    
