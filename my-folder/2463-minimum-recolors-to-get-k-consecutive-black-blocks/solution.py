class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        a = blocks[:k].count('W')
        minVal= a
        for i in range(k,len(blocks)):
            if(blocks[i-k] == 'W'):
                a = a-1
            if(blocks[i] == 'W'):
                a = a+1
            minVal = min(minVal,a)
        return(minVal)
            

        
