class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans, last = [0] * 2, len(nums)
        ans[0], ans[1] = sum(nums)-sum(set(nums)), last * (last+1)//2 - sum(set(nums))
        
        return ans
