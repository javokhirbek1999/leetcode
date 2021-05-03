public class Solution {
    public int[] RunningSum(int[] nums) {
        int[] s = new int[nums.Length];
        s[0] = nums[0];
        for(int i = 1; i<nums.Length; i++){
            s[i] = s[i-1]+nums[i];
        }
        return s;
    }
}
