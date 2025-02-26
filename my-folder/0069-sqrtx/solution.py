class Solution:
    def mySqrt(self, x: int) -> int:
        
        if (x == 0 or x == 1):
            return x
        # k = x//2
        # while(k>0):
        #     if(k*k <= x):
        #         if((k+1) * (k+1) > x):
        #             return k
        #         else:
        #             k = k+1
        #     else:
        #         k = k//2
        y, k = 1, x // 2
        while y <= k:
            mid = (y + k) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                y = mid + 1
                ans = mid  
            else:
                k = mid - 1

        return ans
        
