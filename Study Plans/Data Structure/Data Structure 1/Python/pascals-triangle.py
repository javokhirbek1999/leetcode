class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        tr = []
        
        for i in range(1, numRows+1):
            temp = [0]*i
            temp[0] = 1
            temp[-1] = 1
            
            tr.append(temp)
            
        for i in range(2, len(tr)+1):
            for j in range(1, len(tr[i-1])-1):
                tr[i-1][j] = sum(tr[i-2][j-1:j-1+2])
        
        return tr
            
            
