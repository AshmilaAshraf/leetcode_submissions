class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        res = set()
        n = len(digits)
        for i in range(n):
            if(digits[i]!=0):
                for j in range(n):
                    if(i!=j):
                        for k in range(n):
                            if(k != i and k != j):
                                if(digits[k] & 1):
                                    continue
                                else:
                                    res.add(digits[i]*100+digits[j]*10+digits[k])



        # for i in digits:
        #     if i != 0 :
        #         for j in digits:
        #             # if( j != i):
        #                 for k in digits:
        #                     if(k & 1 ):
        #                         continue
        #                     else:
        #                         # if(k != i and k != j):
        #                             res.add(i*100+j*10+k)
        return(sorted(list(res)))

