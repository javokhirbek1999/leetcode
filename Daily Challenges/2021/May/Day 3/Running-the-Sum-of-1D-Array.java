class Solution {
    public int[] runningSum(int[] nums) {
        int[] s = new int[nums.length];
        s[0] = nums[0];
        for(int i = 1; i<nums.length; i++){
            s[i] = s[i-1]+nums[i];
        }
        return s;
    }
}
