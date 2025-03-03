/**
 * @param {number[]} nums
 * @param {number} pivot
 * @return {number[]}
 */
var pivotArray = function(nums, pivot) {
    let a = [] , b = [] , c = [];
    for(let i of nums){
        if(i<pivot){
            a.push(i);
        }
        else if (i>pivot){
            c.push(i);
        }
        else{
            b.push(i);
        }
    };

    return(a.concat(b.concat(c)))
};
