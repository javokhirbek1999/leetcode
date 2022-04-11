class Solution {
    public boolean containsDuplicate(int[] nums) {
        
        Set<Integer> visited = new HashSet<>();
        
        for (int i = 0; i<nums.length; i++) {
            visited.add(nums[i]);
        }
        
        return visited.size() < nums.length;
    }
}
