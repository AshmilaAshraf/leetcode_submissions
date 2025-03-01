/**
 * @param {number[]} nums
 * @return {number[]}
 */
var applyOperations = function(nums) {
    let arr1 = []
    let arr2 = []
    for(let i=0; i<nums.length; i++){
        if(nums[i] == nums[i+1]){
            nums[i] = nums[i]*2
            nums[i+1] = 0
            nums[i] !=0 ? arr1.push(nums[i]) : arr2.push(nums[i])
        }
        else{
            nums[i] !=0 ? arr1.push(nums[i]) : arr2.push(nums[i])
        }
    
    }
    return arr1.concat(arr2)
};
