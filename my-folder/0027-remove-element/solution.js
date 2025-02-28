/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {
    let count = 0;
    let ind = 0
    for(let i = 0; i<nums.length ; i++) {
        if (nums[i] != val){
            nums[ind] = nums[i]
            ind++
            count++
        }

    }
    
    return count
};
