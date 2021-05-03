/**
 * @param {number[]} nums
 * @return {number[]}
 */
var runningSum = function(nums) {
    var s = [];
    s.push(nums[0])
    for(var i = 1; i<nums.length; i++){
        s.push(s[s.length-1]+nums[i]);
    }
    return s;
};
