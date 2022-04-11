class Solution {
    public int maxSubArray(int[] nums) {
        
        if (nums.length == 1) {
            return nums[0];
        }
        
        int globalMax = min(nums);
        int localMax = globalMax;
        
        for (int i = 0; i<nums.length; i++) {
            if (i == 0) {
                localMax = nums[i];
            } else {
                localMax = Math.max(localMax+nums[i], nums[i]);
            }
            
            globalMax = Math.max(globalMax, localMax);
        }
        
        return globalMax;
    }
    
    public int min(int[] arr) {
        
        int minNum = arr[0];
        
        for (int i: arr) {
            minNum = Math.min(minNum, i);
        }
        
        return minNum;
    }
}
