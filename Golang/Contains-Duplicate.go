/*
  1st Solution:
    Time: O(n log(n))
    Space: O(1)
*/
func containsDuplicate(nums []int) bool {
    sort.Slice(nums, func(i, j int) bool {
        return nums[i]<nums[j]
    })
    
    for i := 0; i<len(nums)-1; i++ {
        if nums[i] == nums[i+1] {
            return true
        }
    }
    return false
}

//-------------------------------------------------

/*
  2nd Solution:
    Time: O(n)
    Space: O(n)
*/
func containsDuplicate(nums []int) bool {
    visited := map[int]int{}
    
    for i := 0; i<len(nums); i++ {
        if visited[nums[i]] == 0 {
            visited[nums[i]]+=1
        } else {
            return true
        }
    }
    return false
}
