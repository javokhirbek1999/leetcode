class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        low = 0
        high = len(numbers)-1
        
        while low <= high:
            
            res = numbers[low]+numbers[high]
            
            if res == target:
                return [low+1, high+1]
            
            if res < target:
                low +=1
            
            if res > target:
                high -=1
        
        
