/*
  Time: O(n log(n))
  Space: O(1)
*/
func findDuplicate(nums []int) int {
    
    sort.Slice(nums, func(i, j int) bool {
        return nums[i]<nums[j]
    })
    
    visited := nums[0]
    
    for i := 1; i<len(nums); i++ {
        if nums[i] == visited {
            return nums[i]
        }
        visited = nums[i]
    }
    return -1
}

//-----------------------------------------------------------------------//

/*
   Time: O(n)
   Space: O(n)
*/

func findDuplicate(nums []int) int {
    
    visited := map[int]int{}
    
    for _, val := range nums {
        if _, exists := visited[val]; exists {
            visited[val]++
        } else {
            visited[val] = 1
        }
    }
    
    for key,_ := range visited {
        if visited[key] > 1 {
            return key
        }
    }
    return -1
}
