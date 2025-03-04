class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n!=0:
            c = n%3
            if c==2:
                return False
            n = n//3
        return True

                # j = 0
                # for i in c:
                #     j = j + 3**i

            
                


        
