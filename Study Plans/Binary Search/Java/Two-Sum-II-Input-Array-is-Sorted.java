class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int low = 0;
        int high = numbers.length-1;
        
        while (low <= high) {
            
            int sum = numbers[low]+numbers[high];
            
            if (sum == target) {
                int[] res = new int[2];
                res[0] = low+1;
                res[1] = high+1;
                return res;
            }
            
            if (sum < target) {
                low++;
            } else {
                high--;
            }
        }
        
        return null;
    }
}
