class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        if(left<10):
            res = list(range(left, 10))
            left = 10
        for i in range(left,right+1):
            num = str(i)
            if('0' in num):
                continue
            flag = True
            for j in num:
                if int(num)%(int(j)) != 0 :
                    flag = False
                    break
            if(flag):
                res.append(i)
        return(res)


