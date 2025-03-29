class Solution:
    def fib(self, n: int) -> int:
        if(n==0 or n==1):
            return n
        x = 0
        y = 1
        i = 2
        while(i<=n):
            k = x+y
            x = y
            y = k
            i+=1
        return k


