func divide(dividend int, divisor int) int {
    
    q := int(dividend/divisor)
    
    maxInt := int(math.Pow(2, 31)-1)
    minInt := int(math.Pow(2, 31)/-1)
    
    if q > maxInt {
        return maxInt
    } else if q < minInt {
        return minInt
    } else {    
        return q
    }
}
