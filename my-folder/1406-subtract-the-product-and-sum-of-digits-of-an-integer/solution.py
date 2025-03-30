class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        num = str(n)
        if(len(num) == 1):
            return 0
        sum = 0
        product = 1
        for i in (num):
            sum+= int(i)
            product *= int(i)
        return(product - sum)

