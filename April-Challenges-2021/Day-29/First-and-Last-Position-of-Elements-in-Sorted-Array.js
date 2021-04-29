/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var searchRange = function(nums, target) {
    var ind = [];
    ind.push(-1);
    ind.push(-1);
    if(nums.length==0){
        return ind;
    }
    for(let i = 0; i<nums.length; i++){
        if(nums[i]==target){
            ind[0] = i;
            break;
        }
    }
    if(ind[0]===-1){
        return ind;
    }
    for(let i = ind[0]; i<nums.length; i++){
        if(nums[i]==target){
            ind[1] = i;
        }
    }
    return ind;
};
