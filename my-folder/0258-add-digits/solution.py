class Solution:
    def addDigits(self, num: int) -> int:
        k = str(num)
        while(len(k)!=1):
            c=0
            for i in k:
                c= c+int(i)
            k = str(c)
        return(int(k))
