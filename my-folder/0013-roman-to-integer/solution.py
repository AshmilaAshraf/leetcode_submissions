class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {'I' : 1, 'V' : 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}        
        num = 0
        numList=''
        for i in s:
            if numList and (dict[i] > dict[numList[-1]]):
                num = num + dict[i] - (2 * dict[numList[-1]])
            else:
                num += dict[i]
            numList += i
        return num
        
