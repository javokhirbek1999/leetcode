class Solution {
public:
    int longestValidParentheses(string s) {
        vector<int>stack;
        stack.push_back(-1);
        int max_pars = 0;
        for(int i = 0; i<s.size(); i++){
            if(s[i]=='('){
                stack.push_back(i);
            }else{
                stack.pop_back();
                if (stack.size()==0){
                    stack.push_back(i);
                }else{
                    max_pars = max(max_pars,i-stack.back());
                }
            }
        }
        return max_pars;
    }
};
