class Solution {
    public boolean isPowerOfThree(int n) {          
        long t = 1;
        if (n == 1){
            return true;
         }
        while (true){
            t=t*3;
            if (t==n){
                return true;
                }else if (t>n){
                 return false;
                }
            }
    }
}
