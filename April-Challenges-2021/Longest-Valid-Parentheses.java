class Solution {
    public int longestValidParentheses(String s) {
        Stack<Integer>stack = new Stack<>();
        stack.push(-1);
        int max_pars = 0;
        for(int i = 0; i<s.length(); i++){
            if(s.charAt(i)=='('){
                stack.push(i);
            }else{
                stack.pop();
                if (stack.size()==0){
                    stack.push(i);
                }else{
                    max_pars = Math.max(max_pars,i-stack.peek());
                }
            }
        }
        return max_pars;
    }
}
