class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        # n = len(nums) // 2
        # setNums = set(nums)
        # if(len(setNums) > n):
        #     return False
        # k = 0
        # for i in setNums:
        #     k = k + nums.count(i)//2

        # return(True if k == n else False)
        dictNums = collections.Counter(nums)
        for i in dictNums.values():
            if i%2 != 0:
                return False
        return True
        
