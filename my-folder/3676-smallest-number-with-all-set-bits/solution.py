class Solution:
    def smallestNumber(self, n: int) -> int:
        k = 0
        i = 0
        while(n>0):
            n = n // 2
            k = k + (2 ** i)
            i = i + 1
        return(k)
        
