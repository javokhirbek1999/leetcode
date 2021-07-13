class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        long max_elem = pow(-2,33);
        for(int i = 0; i<nums.size(); i++){
            if (nums[i]>max_elem){
                max_elem = nums[i];
            }
        }
        int ind = 0;
        for(int i = 0; i<nums.size(); i++){
            if(nums[i]==max_elem){
                ind = i;
                break;
            }
        }
        return ind;
    }
};
