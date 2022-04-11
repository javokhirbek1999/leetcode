class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        
        for (int[] i:matrix) {
            
            int low = 0;
            int high = i.length-1;
            
            while (low<=high) {
                
                int mid = (low+high)/2;
                
                int res = i[mid];
                
                if (res == target) {
                    return true;
                }
                
                if (res < target) {
                    low = mid + 1;
                } else {
                    high = mid - 1;
                }
            }
        }
        return false;
    }
}
