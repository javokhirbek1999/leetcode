class Solution {
    public int arrangeCoins(int n) {
     
        if (n<1) {
            return 0;
        }
        
        if (n==1) {
            return 1;
        }
        
        int current = 1;
        int count = 1;
        
        n--;
        
        int i = 2;
        
        while (n > 0) {
            if (n-i<0) {
                return current;
            }
            current = i;
            count++;
            n-=i;
            i++;
        }
        
        return current;
    }
}
