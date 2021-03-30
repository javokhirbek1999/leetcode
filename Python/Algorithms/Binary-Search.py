class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target >max(nums) or target<min(nums) or target not in nums:
            return -1
        low = 0
        high = len(nums)
        while low<=high:
            mid = (low+high)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>=target:
                high = mid-1
            else:
                low = mid+1
        return -1        
            
