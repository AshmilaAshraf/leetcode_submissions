class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        dictList={}
        for i in dominoes:
            k = frozenset(i)
            if(k in dictList):
                dictList[k]+=1
                
            else:
                dictList[k] = 1
        total = sum(((n*(n-1))//2) for n in dictList.values() if n >= 2)
        return(total)
        
