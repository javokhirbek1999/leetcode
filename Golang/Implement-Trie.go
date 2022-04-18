type Trie struct {
    Char string
    Children map[string]*Trie
    Count int
    End bool
}


func Constructor() Trie {
    trie := &Trie{"", map[string]*Trie{"":nil}, 0, false}
    
    return *trie
}


func (this *Trie) Insert(word string)  {
    
    node := this
    
    for i := 0; i<len(word); i++ {
        if val, exists := node.Children[word[i:i+1]]; exists {
            node = val
        } else {
            newNode := &Trie{word[i:i+1], map[string]*Trie{"":nil}, 0, false}
            node.Children[word[i:i+1]] = newNode
            node = newNode
        }
    }
    
    node.Count++;
    node.End = true
    
}


func (this *Trie) Search(word string) bool {
    
    node := this
    
    for i := 0; i<len(word); i++ {
        if val, exists := node.Children[word[i:i+1]]; exists {
            node = val
        } else {
            return false
        }
    }
    
    if node.End {
        return true
    }
    
    return false
}


func (this *Trie) StartsWith(prefix string) bool {
    
    node := this
    
    c := 0
    
    for i := 0; i<len(prefix); i++ {
        if val, exists := node.Children[prefix[i:i+1]]; exists {
            node = val 
            c++
        } else {
            return false
        }
    }
    
    if node.End {
        if c == len(prefix) {
            return true
        }
        return false
    }
    
    return true
}


/**
 * Your Trie object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Insert(word);
 * param_2 := obj.Search(word);
 * param_3 := obj.StartsWith(prefix);
 */
