class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        vector<int>ind;
        ind.push_back(-1);
        ind.push_back(-1);
        for(int i = 0; i<nums.size(); i++){
            if(nums[i]==target){
                ind[0] = i;
                break;
            }
        }
        if(ind[0]==-1){
            return ind;
        }
        for(int i = ind[0]; i<nums.size(); i++){
            if(nums[i]==target){
                ind[1] = i;
            }
        }
        return ind;
        
    }
};
