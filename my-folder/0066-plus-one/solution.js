/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function(digits) {

    // let i = 1
    // const n = digits.length
    // if(digits[n-1] == 9){
    //     while(i < n + 1) {
    //         if(digits[n-i] == 9) {
    //             if(i == n){
    //                 digits[0] = 0
    //                 digits = [1,...digits]
    //             }
    //             else{
    //                 digits[n-i] = 0
    //                 if(digits[n-i-1] != 9 ){
    //                     digits[n-i-1] = digits[n-i-1] +1
    //                 }
    //             }
    //             i = i+1
    //         }
    //         else{
    //             break
    //         }
    //     }
    //     return digits
    // }
    // else{
    //     digits[n -1] = digits[n -1] + 1
    //     return digits
    // }
        const n = digits.length;
    
    for (let i = n - 1; i >= 0; i--) {
        if (digits[i] === 9) {
            digits[i] = 0;
        } else {
            digits[i]++;   
            return digits;
        }
    }
    
    return [1, ...digits];
};
