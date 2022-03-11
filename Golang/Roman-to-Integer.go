func romanToInt(s string) int {
    
    d := map[string]int{
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    
    result := 0
    prev := ""
    
    for i := len(s)-1; i>-1; i-- {
        current := s[i:i+1]
        if len(prev) == 0 {
            result+=d[current]
        } else {
            if d[prev] > d[current] {
                result -= d[current]
            } else {
                result += d[current]
            }
        }
        prev = current
        
    }
    return result
}
