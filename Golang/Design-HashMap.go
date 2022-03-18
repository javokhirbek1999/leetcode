type MyHashMap struct {
    HashMap map[int]int;
}


func Constructor() MyHashMap {
    hashMap := MyHashMap{map[int]int{}}
    return hashMap
}


func (this *MyHashMap) Put(key int, value int)  {
    this.HashMap[key] = value
}


func (this *MyHashMap) Get(key int) int {
    if value, exists := this.HashMap[key]; exists {
        return value;
    }
    return -1
}


func (this *MyHashMap) Remove(key int)  {
    delete(this.HashMap, key)
}


/**
 * Your MyHashMap object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Put(key,value);
 * param_2 := obj.Get(key);
 * obj.Remove(key);
 */
