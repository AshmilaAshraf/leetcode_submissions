/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfTwo = function(n) {
    if (n == 1 || n == 2) return true;
    if (n%2 != 0){
        return false;
    }

    let i = 2;

    while(i<=n){
        if( i == n){
            return true;
        }
         i = i*2;
    }

    return false
};
