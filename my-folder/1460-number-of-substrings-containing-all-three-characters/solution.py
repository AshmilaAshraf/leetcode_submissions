class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        if(len(set(s)) < 3):
            return(0)

        n = len(s)
        count = 0


        ind = {v: 0 for v in 'abc'}

        # c= max(s.index('a'), s.index('b'), s.index('c')) + 1
        c=0
        # for i in 'abc':
        #     ind[i] = s[:c].count(i)

        # c = window_size 

        for i in range(n - 2): 
            while c < n and (ind['a'] == 0 or ind['b'] == 0 or ind['c'] == 0):
                ind[s[c]] += 1 
                c += 1
            
            if all(value > 0 for value in ind.values()):
                count += n - c + 1 

            ind[s[i]] -= 1
        return count
        # count = 0
        # left = 0
        # freq = {'a': 0, 'b': 0, 'c': 0}
        
        # for right in range(len(s)):
        #     freq[s[right]] += 1  
            
        #     while all(freq.values()):
        #         count += len(s) - right  
        #         freq[s[left]] -= 1
        #         left += 1  
                
        # return count


        # n =len(s)
        # ind = {v: 0 for v in 'abc'}
        # Initial_window_size = max(s.index('a'),s.index('b'),s.index('c')) + 1
        # for i in 'abc':
        #     ind[i] = s[:Initial_window_size].count(i)
        # count = n - Initial_window_size
