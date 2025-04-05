class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if(num == 1):
            return True
        i = 2
        while(i <= num):
            if(i*i <num and ((i+1) * (i+1))>num):
                return False
            if(i*i == num):
                return True
            i += 1

