class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        # def seive(start, n):
        #     primeList = list(range(start, n +1 ))
        #     p =2
        #     while(p * p <n+1):
        #         list2 = list(range(primeList[0], n + 1, p))
        #         primeList = [x for x in primeList if x not in list2]
        #         # for i in primeList:
        #         #     if(i%p == 0):
        #         #         primeList.remove(i)
        #         p = p+1
        #     return primeList

        # if((right==left+1 and right != 3) or right <= 2):
        #     return([-1,-1])
        # else:
        #     # k = left if left % 2 != 0 or left == 2 else left+1
        #     # a=[]
        #     result = [-1,-1]
        #     a = seive(left,right)
        #     if(left <= 2):
        #         a = [2]+a
        #     # while(k<=right):
        #     #     flag = True
        #     #     j=2
        #     #     for i in range(3,k,2):
        #     #         if(k%i == 0):
        #     #             flag = False
        #     #             break
        #     #         if(i*i > right):
        #     #             break
        #     #         # else:
        #     #         #     j = i
        #     #     if(flag):
        #     #         a.append(k)
        #     #     k = k+2
        #     # leftInd = a.index(left)
        #     # rightInd = a.index(right)
        #     if(len(a)>1):
        #         result = [a[0],a[1]]
        #         min_gap = a[1] - a[0]
        #         for i in range(2,len(a)):
        #             if(min_gap > a[i]-a[i-1]):
        #                 min_gap = a[i]-a[i-1]
        #                 result = [a[i-1],a[i]]
        #     return result
        def sieve(n):
            is_prime = [True] * (n + 1)
            is_prime[0] = is_prime[1] = False
            for i in range(2, int(n**0.5) + 1):
                if is_prime[i]:
                    for j in range(i * i, n + 1, i):
                        is_prime[j] = False
            return [i for i in range(2, n + 1) if is_prime[i]]

        primes = sieve(right)

        primes_in_range = [p for p in primes if left <= p <= right]

        if len(primes_in_range) < 2:
            return [-1, -1]

        min_gap = float('inf')
        result = [-1, -1]
        for i in range(len(primes_in_range) - 1):
            gap = primes_in_range[i + 1] - primes_in_range[i]
            if gap < min_gap:
                min_gap = gap
                result = [primes_in_range[i], primes_in_range[i + 1]]

        return result
