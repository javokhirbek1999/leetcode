class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        s = [nums.pop(0)]
        for i in nums:
            s.append(s[-1]+i)
        return s
