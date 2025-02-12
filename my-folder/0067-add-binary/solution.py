class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c = list(a if len(a) >len(b) else b)
        d = list((b if len(b) <len(a) else a).zfill(len(c)))
        carry = False
        for i in range(1,len(c)+1):
            e = c[-i]
            f = d[-i]
            if(carry):
                if(e == f == '1'):
                    c[-i] = '1'
                    carry =True
                elif(e == f == '0'):
                    c[-i] = '1'
                    carry = False
                else:
                    c[-i] = '0'
                    carry = True
            else:
                if(e == f == '1'):
                    c[-i] = '0'
                    carry =True
                elif(e == f == '0'):
                    c[-i] = '0'
                    carry = False
                else:
                    c[-i] = '1'
                    carry = False
        if(carry):
            return('1'+''.join(c))
        else:         
            return(''.join(c))
