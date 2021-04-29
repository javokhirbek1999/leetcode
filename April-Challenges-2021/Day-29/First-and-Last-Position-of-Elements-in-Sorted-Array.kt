class Solution {
    fun searchRange(nums: IntArray, target: Int): IntArray {
        var ind = IntArray(2){-1;-1}
        for(i in nums.indices){
            if(nums[i]==target){
                ind[0] = i
                break
            }
        }
        if(ind[0]==-1){
            return ind
        }
        for(i in nums.indices){
            if(nums[i]==target){
                ind[1] = i
            }
        }
        return ind
    }
}
