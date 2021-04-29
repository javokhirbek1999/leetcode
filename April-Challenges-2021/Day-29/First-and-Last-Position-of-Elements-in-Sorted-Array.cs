public class Solution {
    public int[] SearchRange(int[] nums, int target) {
        int[] ind = new int[2];
        ind[0] = -1;
        ind[1] = -1;
        if(nums.Length==0){
            return ind;
        }
        for(int i = 0; i<nums.Length; i+=1){
            if(nums[i]==target){
                ind[0] = i;
                break;
            }
        }
        if(ind[0]==-1){
            return ind;
        }
        for(int i = ind[0]; i<nums.Length; i+=1){
            if(nums[i]==target){
                ind[1] = i;
            }
        }
        return ind;
    }
}
