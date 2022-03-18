class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        maxNum = nums[0]
        
        # store elements of nums in a dict for constant lookup
        num = {i:i for i in nums}
        
        for i in nums:
            maxNum = max(maxNum, i)
        
        if maxNum < 1:
            return 1
        for i in range(1, maxNum+2):
            if i not in num:
                return i
        
            
            
