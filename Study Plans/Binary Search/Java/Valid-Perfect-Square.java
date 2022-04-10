class Solution {
    public boolean isPerfectSquare(int num) {
        
        if (num >= 0) {
            int t = (int)Math.floor(Math.sqrt(num));
            return t*t==num;
        }
        return false;
    }
}
