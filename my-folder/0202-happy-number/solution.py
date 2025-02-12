class Solution:
    def isHappy(self, n: int) -> bool:
        seen = []
        if(n == 1):
            return True
        else:
            while n not in seen:
                seen.append(n)
                n = sum( int(i)**2 for i in str(n))
                if (n == 1):
                    return True
            return False
        
