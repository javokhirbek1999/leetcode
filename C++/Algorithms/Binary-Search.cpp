class Solution {
public:
    int search(vector<int>& nums, int target) {
        int low = 0;
        int high = nums.size()-1;
        
        while(low<=high) {
            
            int mid = (low+high)/2;
            
            int item = nums[mid];
            
            if (item == target) {
                return mid;
            }
            
            if (item < target) {
                low = mid+1;
            }
            
            if (item > target) {
                high = mid-1;
            }
        }
        
        return -1;
    }
};