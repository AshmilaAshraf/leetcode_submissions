class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        else:
            a, b = 2, 3
            for i in range(3, n ):
                a , b = b, a+b
            return b
