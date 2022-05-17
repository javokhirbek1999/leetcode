class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        
        mx = 1
        
        tree = [0,mx]
        
        d = 0
        prev = mx
        while mx<label:
            mx=(mx*2)+1
            
            if d == 0:
                tree.extend([i for i in range(mx, prev, -1)])
                d = 1
            else:
                tree.extend([i for i in range(prev+1, mx+1)])
                d = 0
                
            prev = mx
        
        ind = tree.index(label)
        
        res = []
        
        while ind > 0:
            res.append(tree[ind])
            if ind%2 != 0:
                ind-=1
                ind = ind//2
            else:
                ind = ind//2
        
        return res[::-1]
    
