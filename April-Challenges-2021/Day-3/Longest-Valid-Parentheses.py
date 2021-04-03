 
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_pars = 0
        stack = []
        stack.append(-1)
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if len(stack)==0:
                    stack.append(i)
                else:
                    max_pars = max(max_pars, i-stack[-1])
        return max_pars     
