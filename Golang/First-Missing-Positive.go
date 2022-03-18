/*
  Time: O(n)
  Space: O(n)
*/
func firstMissingPositive(nums []int) int {
    maxNum := nums[0]
    
    num := map[int]int{}
    
    for i := 0; i<len(nums); i++ {
        if nums[i] > maxNum {
            maxNum = nums[i];
        }
        num[nums[i]] = nums[i]
    }
    
    if maxNum < 1 {
        return 1
    }
    
    for i := 1; i<maxNum+2; i++ {
        if _, exists := num[i]; !exists {
            return i
        }
    }
    return -1
}
