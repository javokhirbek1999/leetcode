func tribonacci(n int) int {
    
    if n == 0 {
        return 0
    }
    
    if n == 1 {
        return 1
    }
    
    if n == 2 {
        return 1
    }
    
    if n == 3 {
        return 2
    }
    
    t1,t2,t3 := 1,1,2
    
    sum := 0
    
    for i := 2; i<n-1; i++ {
        sum = t1+t2+t3
        t1 = t2
        t2 = t3
        t3 = sum
    }
    
    return sum
}
