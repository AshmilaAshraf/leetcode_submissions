class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        a, c = [],[]
        b= 0
        for i in nums:
            if(i<pivot):
                a.append(i)
            
            elif (i>pivot):
                c.append(i)
            
            else:
                b = b+1
        b = [pivot]*b
        return(a+b+c)
        
