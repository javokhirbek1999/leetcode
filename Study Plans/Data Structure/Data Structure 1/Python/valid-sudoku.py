from collections import Counter
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        d = {str(i):i for i in range(1,10)}
        
        for i in board:
            visited = {}
            for j in i:
                if j in d and j not in visited:
                    visited[j] = 1
                else:
                    if j in visited:
                        return False
        
        for i in range(9):
            visited = {}
            t = 0
            while True:
                temp = board[t][i]
                if temp in d and temp not in visited:
                    visited[temp] = 1
                else:
                    if temp in visited:
                        return False
                    
                t+=1
                if t == 9:
                    break
        
        
        k, l, t = 0, 0, 0
        ts = []
        while True:
            nums = []
            for i in range(k,k+3):
                for j in range(l, l+3):
                    temp = board[i][j]
                    if temp in d:
                        nums.append(int(temp))
            ts.append(set(Counter(nums).values()))
            if k != 6:
                k+= 3
            else:
                k = 0
                t+=1
            
            if t == 1:
                l = 3
            
            if t == 2:
                l = 6
            if t == 3:
                l = 9
            
            if t == 3 and l == 9:
                break
        
        for i in ts:
            if len(i)>0:
                if len(i) != 1 or i.pop() != 1:
                    return False
        return True
