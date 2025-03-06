class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer=[]
        if(n<3):
            answer = [str(i) for i in range(1,n+1)]
            return(answer)
        for i in range(1,n+1):
            if(i%3==0 or i%5==0):
                if(i%15 == 0):
                    answer.append("FizzBuzz")
                elif(i%5==0):
                    answer.append("Buzz")
                else:
                    answer.append("Fizz")
            else:
                answer.append(str(i))
        return(answer)
