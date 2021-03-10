class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res = res ^ i
        return res
        
