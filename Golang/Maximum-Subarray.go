func maxSubArray(nums []int) int {
    
    if len(nums) == 1 {
        return nums[0]
    }
    
    global, local := getMin(nums), getMin(nums)
    
    for index, value := range nums {
        if index == 0 {
            local = nums[0]
        } else {
            local = max(local+value, value)
        }
        global = max(global, local)
    }
    
    return global
}

func max(a int, b int) int {
    if a > b {
        return a
    } else {
        return b
    }
}

func getMax(nums []int) int {
    res := nums[0]
    
    for _, value := range nums {
        if res < value {
            res = value
        }
    }
    
    return res
}

func getMin(nums []int) int {
    res := nums[0]
    
    for _, value := range nums {
        if res > value {
            res = value
        }
    }
    return res
}
