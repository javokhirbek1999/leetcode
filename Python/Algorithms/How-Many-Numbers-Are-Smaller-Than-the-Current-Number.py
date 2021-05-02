class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        t = []
        for i in range(len(nums)):
            c = 0
            for j in range(len(nums)):
                if nums[i]>nums[j] and i!=j:
                    c+=1
            t.append(c)
        return t
