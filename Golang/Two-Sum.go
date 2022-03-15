/*
  Time: O(n)
  Space: O(n)
*/
func twoSum(nums []int, target int) []int {
    
    m := make(map[int]int)
    
    for i := 0; i<len(nums); i++ {
        
        comp := target-nums[i]
        
        if val, exists := m[comp]; exists {
            pairs := []int{}
            pairs = append(pairs, val)
            pairs = append(pairs, i)
            return pairs
        }
        
        m[nums[i]] = i
    }
    return []int{}
}
