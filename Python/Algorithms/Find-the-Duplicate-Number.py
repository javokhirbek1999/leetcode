# Time: (n log(n))
# Space: O(1)

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        
        visited = nums[0]
        for i in range(1, len(nums)):
            if visited == nums[i]:
                return nums[i]
            visited = nums[i]

            
#------------------------------------------------------------------------#

# Time: O(n)
# Space: O(n)

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        visited = {}
        
        for i in nums:
            if i in visited:
                visited[i]+=1
            else:
                visited[i] = 1
        
        for i in visited.keys():
            if visited[i]>1:
                return i
