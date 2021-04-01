import java.util.Stack;

class MinStack {
    Stack<Integer> stack;
    Stack<Integer> minimum;
    /** initialize your data structure here. */
    public MinStack() {
        this.stack = new Stack<>();
        this.minimum = new Stack<>();
    }

    public void push(int val) {
        if(stack.size()==0){
            stack.push(val);
            minimum.push(val);
        }else{
            if (minimum.get(minimum.size()-1)>val){
                minimum.push(val);
            } else {
                minimum.push(minimum.get(minimum.size()-1));
            }
            stack.push(val);
        }
    }

    public void pop() {
        stack.pop();
        minimum.pop();
    }

    public int top() {
        if(stack.size()==0){
            return -1;
        }
        return stack.get(stack.size()-1);
    }

    public int getMin() {
        if(minimum.size()==0){
            return -1;
        }
        return minimum.get(minimum.size()-1);
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */
