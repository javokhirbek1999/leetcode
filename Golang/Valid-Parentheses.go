func isValid(s string) bool {
    
    t := []string{}
    
    for i := 0; i<len(s); i++ {
        
        currentElem := s[i:i+1]

        if len(t) == 0 {
            t = append(t, currentElem)
        } else {
            
            lastElem := string(t[len(t)-1])
            
            if lastElem == "(" && currentElem == ")" {
                t = t[:len(t)-1]
            } else if lastElem == "[" && currentElem == "]" {
                t = t[:len(t)-1]
            } else if lastElem == "{" && currentElem == "}" {
                t = t[:len(t)-1]
            } else {
                t = append(t, currentElem)
            }
        }
        
    }
    return len(t) == 0   
}
