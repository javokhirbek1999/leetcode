type Node struct {
    Val int
    Next *Node
}

type LinkedList struct {
    Head *Node
    Tail *Node
    Size int
}

func (this *LinkedList) Append(val int) {
    
    node := &Node{val, nil}
    
    if this.Head == nil {
        this.Head = node
        this.Tail = node
    } else {
        this.Tail.Next = node
        this.Tail = this.Tail.Next
    }
    
    this.Size++
}

func (this *LinkedList) Prepend(val int) {
    
    node := &Node{val, nil}
    
    if this.Head == nil {
        this.Head = node
        this.Tail = node
    } else {
        node.Next = this.Head
        this.Head = node
    }
    
    this.Size++
}

func (this *LinkedList) PopLeft() *Node {
    if this.Size>0 {
        temp := this.Head
        this.Head = this.Head.Next
        this.Size--
        return temp
    }
    return &Node{0,nil}
}

type MyCircularQueue struct {
    Queue *LinkedList
    Size int
    MaxSize int
}


func Constructor(k int) MyCircularQueue {
    
    queue := MyCircularQueue{&LinkedList{nil,nil,0}, 0, k}
    return queue
}


func (this *MyCircularQueue) EnQueue(value int) bool {
    if this.Size+1 <= this.MaxSize {
        this.Queue.Append(value)
        this.Size++
        return true
    }
    return false
}


func (this *MyCircularQueue) DeQueue() bool {
    if this.Size > 0 {
        this.Queue.PopLeft()
        this.Size--
        return true
    }
    return false
}


func (this *MyCircularQueue) Front() int {
    if this.Size > 0 {
        return this.Queue.Head.Val
    }
    return -1
}


func (this *MyCircularQueue) Rear() int {
    if this.Size > 0 {
        return this.Queue.Tail.Val
    }
    return -1
}


func (this *MyCircularQueue) IsEmpty() bool {
    return this.Size == 0
}


func (this *MyCircularQueue) IsFull() bool {
    return this.Size == this.MaxSize
}

// [1,2,3]
/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * obj := Constructor(k);
 * param_1 := obj.EnQueue(value);
 * param_2 := obj.DeQueue();
 * param_3 := obj.Front();
 * param_4 := obj.Rear();
 * param_5 := obj.IsEmpty();
 * param_6 := obj.IsFull();
 */
