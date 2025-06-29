class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count = 0
        # listParanthesis = []
        # sample=''
        # result = ''
        res = ''
        # if n == 0:
        #     return s
        for i in range(len(s)):
            if s[i] == '(':
                if(count>0):
                    res+=s[i]
                count+=1

            else:
                count -= 1
                if(count>0):
                    res+=s[i]

        return res
            # sample += s[i]
            # if count == 0:
            #     listParanthesis.append(sample)
            #     sample = ''
            
            
                
        # for i in listParanthesis:
        #     result += i[1:len(i)-1]
        # return result



