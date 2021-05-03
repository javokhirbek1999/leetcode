class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        vector<int>s;
        s.push_back(nums[0]);
        for(int i = 1; i<nums.size(); i++){
            s.push_back(s[s.size()-1]+nums[i]);
        }
        return s;
    }
};
