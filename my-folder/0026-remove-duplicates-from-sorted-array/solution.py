class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = [nums[0]]
        for i in range(1,len(nums)):
            if (nums[i] == nums[i-1]):
                continue 
            else:
                n = n+ [nums[i]]
        nums[:len(n)] = n
        return(len(n))

