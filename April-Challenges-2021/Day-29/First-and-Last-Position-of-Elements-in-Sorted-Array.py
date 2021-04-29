class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first,second = -1,-1
        if len(nums)==0 or target not in nums:
            return [first,second]
        for i in range(len(nums)):
            if nums[i] == target:
                first = i
                break
        for i in range(first,len(nums)):
            if nums[i] == target:
                second = i
        return [first,second]
